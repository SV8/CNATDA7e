from socket import *
import datetime
serverName = '103.91.219.180'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
message = 'I ping you!'
for var in list(range(10)):
	try:
		t0 = datetime.datetime.now()
		clientSocket.sendto(message.encode(), (serverName, serverPort))
		echoMessage, serverAddress = clientSocket.recvfrom(1024)
		t1 = datetime.datetime.now()
		timeElapsed = t1 - t0
		print('Ping', var, timeElapsed.microseconds/1000, 'ms')
	except Exception as e:
		print('Ping', var, 'Request timed out.')
clientSocket.close()
