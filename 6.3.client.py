import socket

ClientSocket = socket.socket()
host = '192.168.56.110'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response)


while True:

    print("\n\t\tMAIN MENU\n\n")
    func=input("\t[1] for Calculate LOG \n\t[2] for Calculate Square Root \n\t[3] for Calculate  Exponential Function.\n\tEnter [exit] to terminate: \n\nMenu:  ")
    if(func=='1'):
        result=input("[?] Number:")
    elif(func=='2'):
        result=input("[?] Number:")
    elif(func=='3'):
        result=input("[?] Number:")
    elif(func=='exit'):
        break

    message=func+" "+result
    ClientSocket.send(str.encode(message))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()
