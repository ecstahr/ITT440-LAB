import socket
import os
import sys

#host server ip 
ip = "192.168.56.110"

#socket creating
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8888

s.connect((ip, PORT))

sendFile = input("\n[?] Enter name of file to send: ")
file = open(sendFile, "rb")
sendData = file.read(1024)

s.send(sendFile.encode("utf-8"))

while sendData:
	msg=s.recv(1024)
	print("[+]Message received!\n")
	print(msg.decode("utf-8"))
	print("File name: " + sendFile)

	s.send(sendData)
	sendData = file.read(1024)

#close socket
s.close()
