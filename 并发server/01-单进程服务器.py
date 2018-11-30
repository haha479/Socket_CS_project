import socket

#创建套接字
tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定地址
server_addr = ("",8899)
tcp_socket.bind(server_addr)

#监听状态,设置最大连接数
tcp_socket.listen(5)

while True :
	#被动待链接状态
	new_socket,client_addr = tcp_socket.accept()
	while True :
		#接收数据
		recv_info = new_socket.recv(1024)
		print("%s:%s"%(str(client_addr),recv_info.decode("gb2312")))

new_socket.close()
tcp_socket.close()