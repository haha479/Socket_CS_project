from socket import *
from threading import Thread

def recv_content(new_socket,client_addr):
	while True :
		recv_info = new_socket.recv(1024)
		print("%s:%s"%(str(client_addr),recv_info.decode("gb2312")))

def main():
	tcp_server = socket(AF_INET,SOCK_STREAM)

	tcp_server.bind(("",9090))

	tcp_server.listen(5)

	while True :
		new_socket,client_addr = tcp_server.accept()

		#创建线程
		th = Thread(target=recv_content,args=(new_socket,client_addr))
		th.start()
	tcp_server.close()

if __name__ == '__main__':
	main()