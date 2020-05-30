from socket import * 
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver 
mailserver = 'smtp.126.com'

# Create socket called clientSocket and establish a TCP connection with mailserver 
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
 	print('220 reply not received from server.')

# Send HELO command and print server response. 
heloCommand = 'HELO Alice\r\n' 
clientSocket.send(heloCommand.encode()) 
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
	print('250 reply not received from server.')

# Authentication
authCommand = 'AUTH LOGIN\r\n'
clientSocket.send(authCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '334':
	print('334 reply not received from server.')

clientSocket.send('dml2aXRvQDEyNi5jb20=\r\n'.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '334':
	print('334 reply not received from server.')

clientSocket.send('eHNzczE5ODExMjM=\r\n'.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '250':
	print('334 reply not received from server.')

# Send MAIL FROM command and print server response. 
clientSocket.send('MAIL FROM: <vivito@126.com>\r\n'.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
	print('250 reply not received from server.')

# Send RCPT TO command and print server response.
clientSocket.send('RCPT TO: <13329765@qq.com>\r\n'.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '250':
	print('250 reply not received from server.')

# Send DATA command and print server response.
clientSocket.send('DATA\r\n'.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7)
if recv7[:3] != '250':
	print('250 reply not received from server.')

# Send message data.
header = '''
from:vivito@126.com
to:1329765@qq.com
subject:hello!!!
Content-Type:text/plain
'''
clientSocket.send((header + msg + endmsg).encode())
recv8 = clientSocket.recv(1024).decode()
print(recv8)
if recv8[:3] != '250':
	print('250 reply not received from server.')

# # Send QUIT command and get server response.
clientSocket.send('QUIT\r\n'.encode())
recv9 = clientSocket.recv(1024).decode()
print(recv9)
