
import grpc
from concurrent import futures
import time

#import generated class
from gRPC_service.proto import checkPrime_pb2
from gRPC_service.proto import checkPrime_pb2_grpc

#import original class
from src.primeNumber import validatePrime

class CheckPrimeServiceServicer(checkPrime_pb2_grpc.CheckPrimeServiceServicer):

    def ValidatePrime(self, request, context):
        response = checkPrime_pb2.outputResponse()
        response.result = validatePrime(request.number)

        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

checkPrime_pb2_grpc.add_CheckPrimeServiceServicer_to_server(CheckPrimeServiceServicer(),server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)