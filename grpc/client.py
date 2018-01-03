"""
Description: This file is a test example of realizing the grpc communication between
             aws cloud and a local computer.
"""
import grpc

import bfawstest_pb2
import bfawstest_pb2_grpc

_REQ_MSG = dict(testtextmessage=input("Input the request message:\n"))

def run():
    """
    Define the run program.
    """
    channel = grpc.insecure_channel('52.38.18.139:22222')
    stub = bfawstest_pb2_grpc.TestAWSServiceStub(channel)
    response = stub.Getdatabase(bfawstest_pb2.awsrequest(**_REQ_MSG))
    print(response)

if __name__ == "__main__":
    run()
