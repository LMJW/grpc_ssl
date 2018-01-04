"""
Simple grpc server module
"""
from concurrent import futures
import time
import sqlite3

import bfawstest_pb2
import bfawstest_pb2_grpc

import grpc

_SERVER_KEYS = dict(private_key_certificate_chain_pairs=\
                    [(open('../out/server.key').read().encode(),\
                      open('../out/server.crt').read().encode())],\
                    root_certificates=None, require_client_auth=False)

def request_to_sql(db_file, request):
    """
    This function stores the request into a sqlite3 database
    """
    db_cursor = db_file.cursor()
    try:
        db_cursor.execute('''CREATE table IF NOT EXISTS request (Time, info)''')
        db_cursor.execute('INSERT INTO request VALUES ("%s", "%s")'%\
            (time.ctime(), request.testtextmessage))
        # get the query results from database
        try:
            db_cursor.execute('SELECT _rowid_, * FROM request')
            _datalist = []
            while True:
                _numorder, _time, _info = db_cursor.fetchone()
                print(_numorder, _time, _info)
                _datalist.append(bfawstest_pb2.COUNTERANDTIMER(\
                        orderofrequest=_numorder, requesttime=_time, requestinfo=_info))
        except TypeError as err:
            print(err)
            _response = bfawstest_pb2.awsresponse(responsemsg="Query successfully",\
                    countertimer=_datalist)
            return _response
    except sqlite3.OperationalError as e:
        print(e)
        return bfawstest_pb2.awsresponse(responsemsg="Sever database query error")

class AWSQueryService(bfawstest_pb2_grpc.TestAWSServiceServicer):
    """
    This class defines the simple aws query service
    """
    def __init__(self):
        """
        Attach the database to the class
        """
        # self.db = sqlite3.connect('test.db')
        # Direct connect to database does not support concurrency,
        # so I change this into a memory format.
        self.db = sqlite3.connect(":memory:", check_same_thread=False)

    def Getdatabase(self, request, context):
        """
        The service source code
        """
        return request_to_sql(self.db, request)

def serve():
    """
    The server program.
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    bfawstest_pb2_grpc.add_TestAWSServiceServicer_to_server(AWSQueryService(), server)
    credential = grpc.ssl_server_credentials(**_SERVER_KEYS)
    server.add_secure_port('[::]:22222', credential)
    server.start()
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
