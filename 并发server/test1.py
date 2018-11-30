from socket import *

#创建套接字
tcp_server = socket(AF_INET,SOCK_STREAM)

tcp_server.bind(("",8899))

#设置套接字不堵塞
tcp_server.setblocking(False)

tcp_server.listen(1000)

#创建列表用来放套接字和客户端信息
client_info = []
while True :

	try :
		client_socket,client_addr = tcp_server.accept()
	except:
		print("出错啦!")
		pass
	else :
		print("欢迎新用户!")
		client_info.append((client_socket,client_addr))

	for socket,addr in client_info :
		try :
			#接收数据
			recv_data = socket.recv(1024)
		except :
			pass
		else :

			if len(recv_data) > 0 :
				print("%s:%s"%(str(addr),recv_data.decode("gb2312")))
			else :
				print("用户退出了")
				socket.close()
				break