from socket import *

#设置套间字不堵塞来达到并发服务器效果
#访问量不是很大的情况下可以使用,如果访问量大了,性能就会有问题
tcp_server = socket(AF_INET,SOCK_STREAM)
#绑定
tcp_server.bind(("",9098))
#设置tcp-server非堵塞
tcp_server.setblocking(False)
#监听
tcp_server.listen(5)

#创建列表用来放套间字和地址信息
info_list = []
while True :
	try :
		new_socket,client_addr = tcp_server.accept()
	except:
		pass
	#如果没有报错则就是有新客户链接了
	else :
		#设置new_socket为非阻塞
		new_socket.setblocking(False)
		print("欢迎新客户:%s"%str(client_addr))
		info_list.append((new_socket,client_addr))
	#将信息列表遍历出来
	for client_socket,client_addr in info_list:
		try :
			recv_data = client_socket.recv(1024)
		except:
			pass
		else :
			if len(recv_data) > 0 :
				print("客户:%s 请求内容:%s"%(str(client_addr),recv_data.decode("gb2312")))
			else :
				client_socket.close()

