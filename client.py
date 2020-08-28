from gRPC_service.proto import checkPrime_pb2_grpc,checkPrime_pb2
import grpc


channel = grpc.insecure_channel("localhost:50051")


stub = checkPrime_pb2_grpc.CheckPrimeServiceStub(channel)

request = checkPrime_pb2.inputRequest(number=7)

response = stub.ValidatePrime(request)

print(response.result)

