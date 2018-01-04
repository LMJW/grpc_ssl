"""
Description: This file is a test example of realizing the grpc communication between
             aws cloud and a local computer.
"""
import grpc

import bfawstest_pb2
import bfawstest_pb2_grpc

_REQ_MSG = dict(testtextmessage=input("Input the request message:\n"))

_CLIENT_KEYS = dict(root_certificates=open('../out/server.crt').read().encode(),
                    private_key=None,#open('../out/client.crt').read().encode(),
                    certificate_chain=None)

def run():
    """
    Define the run program.
    """
    # SSH secure channel
    creds = grpc.ssl_channel_credentials(**_CLIENT_KEYS)
    channel = grpc.secure_channel('server:22222', creds)
    # channel = grpc.insecure_channel('52.38.18.139:22222')
    stub = bfawstest_pb2_grpc.TestAWSServiceStub(channel)
    response = stub.Getdatabase(bfawstest_pb2.awsrequest(**_REQ_MSG))
    print(response)

if __name__ == "__main__":
    run()
