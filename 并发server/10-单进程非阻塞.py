from socket import *

#创建套接字
tcp_server = socket(AF_INET,SOCK_STREAM)

#绑定服务器地址
tcp_server.bind(("",8080))

#设置不阻塞
tcp_server.setblocking(False)

#进入监听状态
tcp_server.listen(100)

#定义列表来放客户端和套接字信息
info_list = []
while True :
	try :
		new_socket,client_addr = tcp_server.accept()
	except :
		pass
	#如果没有报错说明新客户端连接上了
	else :
		print("欢迎客户:%s"%str(client_addr))
		#设置不堵塞
		new_socket.setblocking(False)
		#将客户端返回的套接字装在列表
		info_list.append((new_socket,client_addr))
	#遍历含有套接字和地址信息的列表
	for sock,addr in info_list :
		try :
			#接受请求信息
			recv_data = sock.recv(1024)
		except :
			pass
		else :
			if recv_data :
				print("%s:%s"%(str(addr),recv_data.decode("gb2312")))
			else :
				print("%s客户端关闭了链接" % str(addr))
				sock.close()

tcp_server.close()
