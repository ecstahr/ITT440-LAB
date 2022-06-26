import socket
import sys
import time
import math
import errno
from multiprocessing import Process



def calcLOG(i):
	print("\nYou have chosen calculation for Log:",i)
	i=float(i)
	ans=math.log(i)
	print("\nAnswer:",ans)
	return ans


def calcSquareRoot(i):
	print("\nYou have chosen calculation for Square Root:",i)
	i=float(i)
	ans=math.sqrt(i)
	print("\nAnswer:",ans)
	return ans


def calcExponentialFunction(i):
	print("\nYou have chosen calculation for Exponential Function:",i)
	i=float(i)
	ans=math.exp(i)
	print("\nAnswer:",ans)
	return ans


def process_start(s_sock):
	s_sock.send(str.encode('-------Python  Online Calculator-------'))

	while True:
		data = s_sock.recv(2048)
		data=data.decode('utf-8')
		try:
			func,result=data.split(" ",2)
		except:
			print("[!] Data not received\n")
			break

		#if not data:
		#	break


		if(func=='1'):
			ans=calcLOG(result)
		elif(func=='2'):
			ans=calcSquareRoot(result)
		elif(func=='3'):
			ans=calcExponentialFunction(result)
		elif(func=='exit'):
			break

		equal="\n[=] Answer: %s\n"% str(ans)


		s_sock.sendall(str.encode(equal))
	s_sock.close()


if __name__ == '__main__':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("",8888))
	print("[~] Waiting for incoming connections")
	s.listen(3)
	try:
		while True:
			try:
				s_sock, s_addr = s.accept()
				p = Process(target=process_start, args=(s_sock,))
				p.start()

			#catches socket error
			except socket.error:
				print("[!] Socket error!\n")

	#catches exception error
	except Exception as e:
		print("[!] Exception error! \n")
		print(e)
		sys.exit(1)
	finally:
		s.close()
