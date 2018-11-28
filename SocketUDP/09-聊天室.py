import socket

from time import ctime

udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_socket.bind(("",2626))

#写个循环可以一直接收和发送消息
while True :
	recv_data, recv_address = udp_socket.recvfrom(1024)

	#返回对方的信息发给对方
	udp_socket.sendto(recv_data,recv_address)
	#打印对方的信息和发送过来的内容
	print("[%s],ip:%s,content:%s"%(ctime(),recv_address[0],recv_data.decode("gb2312")))

