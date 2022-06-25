import socket
import sys

#socket object creating
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8888

s.bind(('', PORT))
print("Socket successfully binded\n")
#listening  to any incoming connections
s.listen(5)
print('\nWaiting for incoming connection...')

while True:
	c, addr = s.accept()
	print("[!] Connected to client.\n")

	filename= c.recv(1024)
	file= open(filename, "wb")

	msg= "You are now connected to: " + addr[0]
	c.send(msg.encode("utf-8"))

	#receive data from client
	recvdata= c.recv(1024)
	while recvdata:
		file.write(recvdata)
		recvdata = c.recv(1024)

	#close file
	file.close()
	print("[+]File has been copied and stored successfully.\n")

	#close connection
	c.close()
	print("Connection closed.\n")

	break
