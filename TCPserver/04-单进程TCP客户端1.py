from socket import *

#创建套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)

#与服务器进行链接
server_addr = ("192.168.16.90",8890)
tcp_socket.connect(server_addr)

while True :
	#向服务器发送数据
	send_info = input("发送到服务器的数据:")
	tcp_socket.send(send_info.encode("utf-8"))
