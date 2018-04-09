'''import socket

from threading import Thread
server_socket=socket.socket()
server_socket.bind(("",1234))
server_socket.listen(5)
d={}
for i in range(3):
	conn,addr=server_socket.accept()
	name=conn.recv(1000)
	d[name.decode()]=conn
l=[]
for k in d:
	l.append(k)

def f1():
	while True:
		data=d[l[0]].recv(1000)
		data=data.decode()
		data=data+'##'+l[0]
		d[l[1]].sendall(data.encode())
		d[l[2]].sendall(data.encode())

def f2():
	while True:
		data=d[l[1]].recv(1000)
		data=data.decode()
		data=data+'##'+l[1]
		d[l[0]].sendall(data.encode())
		d[l[2]].sendall(data.encode())

def f3():
	while True:
		data=d[l[2]].recv(1000)
		data=data.decode()
		data=data+'##'+l[2]
		d[l[0]].sendall(data.encode())
		d[l[1]].sendall(data.encode())


t1=Thread(target=f1)
t2=Thread(target=f2)
t3=Thread(target=f3)
t1.start()
t2.start()
t3.start()
##conn.sendall(b"Hi from server")'''
import socket
from threading import Thread

server=socket.socket()
server.bind(("",1234))
server.listen(10)

clients={}

def client_thread(name,conn,addr):
	while True:
		data=conn.recv(1000)
		message=data.decode()
		message=name+":"+message
		for client_name in clients:
			if client_name!=name:
				clients[client_name].sendall(message.encode())
while True:
	conn,addr=server.accept()
	name=conn.recv(1000)
	name=name.decode()
	clients[name]=conn
	t=Thread(target=client_thread,args=(name,conn,addr))
	t.start()