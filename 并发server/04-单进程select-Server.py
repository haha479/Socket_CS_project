from socket import *
import select
tcp_server = socket(AF_INET,SOCK_STREAM)

tcp_server.bind(("",8990))

tcp_server.listen(5)

socket_list = [tcp_server]

while True :

	#阻塞的等待
	readable,writeable,exceptional = select.select(socket_list,[],[])

	#开始读数据
	for sock in readable:
		#如果检测到有可以读取数据的套件字
		if sock == tcp_server:
			new_socket,client_addr = tcp_server.accept()
			#把新的套间字装到列表中
			socket_list.append(new_socket)
		#否则就是已经可以直接取数据的套间字的了
		else:
			recv_info = sock.recv(1024)
			print(client_addr,recv_info.decode("gb2312"))
tcp_server.close()


