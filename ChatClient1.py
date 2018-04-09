import socket
from threading import Thread
client_socket=socket.socket()
client_socket.connect(("127.0.0.1",1234))
#print(client_socket)
send=""

send=input("Enter your name:")
client_socket.sendall(send.encode())

def f1(): ##f1 is used to send
	global send
	while True:
		send=input("")
		s=send.encode() #converts everything to bytes
		client_socket.sendall(s)
def f2(): ##f2 is used to receive
	while True:
		data=client_socket.recv(1000)
		#data=data.decode()
		#lst=data.split("##")
		#print(lst[1]+":"+lst[0])
		print(data.decode())
#client_socket.sendall(b"Hi from client")
if __name__=="__main__":
	t2=Thread(target=f2)
	t2.start()
	f1()