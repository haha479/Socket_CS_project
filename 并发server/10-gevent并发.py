import gevent
from gevent import socket,monkey
monkey.patch_all()

def recv_data(client_socket,client_addr):
	while True :

		#接收数据并打印
		recv_info = client_socket.recv(1024)

		#如果客户端断开了链接
		if len(recv_info)>0:
			print("%s:%s"%(str(client_addr),recv_info.decode("gb2312")))
		else :
			client_socket.close()
			break

def main():

	a = socket.socket()

	a.bind(("",6788))

	a.listen(5)

	while True :

		client_socket,client_addr = a.accept()

		gevent.spawn(recv_data,client_socket,client_addr)

if __name__ == '__main__':
	main()
