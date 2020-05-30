#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#prepare a server socket
serverPort = 12000
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
	#Establish the connection
	print('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(2048).decode()
		fileName = message.split()[1]
		print(fileName, 'requested.')
		f = open(fileName[1:])
		outputData = f.readlines()
		#Send one HTTP header line into socket
		headerLine = 'HTTP/1.1 200 OK\r\n\r\n'
		connectionSocket.send(headerLine.encode())
		#Send the content of requested file to the client
		for i in range(0, len(outputData)):
			connectionSocket.send(outputData[i].encode())
		connectionSocket.close()
	except IOError:
		#Send response message for the file not found
		headerLine = 'HTTP/1.1 404 Not Found\r\n\r\n'
		connectionSocket.send(headerLine.encode())
		respMessage = '''
		<html>
		<head><title>404 Not Found</title></head>
		<body>
		<center><h1>404 Not Found</h1></center>
		<hr><center>REAL Web Server 0.1 alpha</center>
		</body>
		</html>
		'''
		connectionSocket.send(respMessage.encode())
		#Close client socket
		connectionSocket.close()
