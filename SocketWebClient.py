from socket import *
serverName = "103.91.219.180"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
fileName = input("Url you would get: ")
request = "GET " + fileName + " HTTP/1.1/r/n"
request = request + "Host: www.joeplayingmc.com"
print(request)
clientSocket.send(request.encode())
response = clientSocket.recv(2048)
print(response.decode())
