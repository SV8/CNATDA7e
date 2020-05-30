from socket import * 
from os import path
import sys

if len(sys.argv) <= 1:
	print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
	sys.exit(2)

# Create a server socket, bind it to a port and start listening 
proxyServerSocket = socket(AF_INET, SOCK_STREAM) 
proxyServerSocket.bind(('', 12000))
proxyServerSocket.listen(1)

while True:
	# Strat receiving data from the client 
	print('Ready to serve...')
	clientSocket, addr = proxyServerSocket.accept() 
	print('Received a connection from:', addr)
	message = clientSocket.recv(1024).decode()
	print('message:', message)
	# Extract the file name from the given message 
	print('message.split()[1]:', message.split()[1])
	fileName = message.split()[1].partition("/")[2]
	print('fileName:', fileName)
	
	if path.exists(fileName):
		try:
			# Check wether the file exist in the cache
			file = open(fileName, "r")
			outputData = file.readlines()
			fileExist = "true"
			# ProxyServer finds a cache hit and generates a response message 
			clientSocket.send("HTTP/1.0 200 OK\r\n".encode())
			clientSocket.send("Content-Type:text/html\r\n".encode())
			clientSocket.send("\r\n".encode())
			for i in range(0, len(outputData)):
				clientSocket.send(outputData[i].encode())
			print('*CACHE* File found.')
		except IOError:
			# Error handling for file not found in cache
			print('*CACHE* File found, but there is reading error.')
			webServerName = fileName.partition("/")[0]
			reqFileName = "/" + fileName.partition("/")[2]
			print('webServerName:', webServerName)
			print('reqFileName:', reqFileName)
			
			proxyClientSocket = socket(AF_INET, SOCK_STREAM)
			proxyClientSocket.connect((webServerName, 80))
			proxyClientSocket.send(("GET /" + reqFileName + " HTTP/1.1\r\nHost: google.com\r\n\r\n").encode())
			buf = proxyClientSocket.recv(2048)
			print(buf)
			tmpFile = open("./" + fileName, "w+")
			for i in range(0, len(buf)):
				tmpFile.write(buf[i])
				clientSocket.send(buf[i])
			tmpFile.close()
			proxyClientSocket.close()
		clientSocket.close()
	else:
		print('*CACHE* File NOT found.')
		webServerName = fileName.partition("/")[0]
		reqFileName = "/" + fileName.partition("/")[2]
		print('webServerName:', webServerName)
		print('reqFileName:', reqFileName)
		
		proxyClientSocket = socket(AF_INET, SOCK_STREAM)
		proxyClientSocket.connect((webServerName, 80))
		proxyClientSocket.send(("GET /" + reqFileName + " HTTP/1.1\r\nHost: google.com\r\n\r\n").encode())
		buf = proxyClientSocket.recv(2048)
		print(buf)
		tmpFile = open("./" + fileName, "w+")
		for i in range(0, len(buf)):
			tmpFile.write(buf[i])
			clientSocket.send(buf[i])
		tmpFile.close()
		proxyClientSocket.close()
		clientSocket.close()
	proxyServerSocket.close()