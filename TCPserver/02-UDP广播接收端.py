import socket

udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#绑定地址
server_addr = ("",8080)
udp_socket.bind(server_addr)
for x in range(5):
	#打印接收的内容
	recv_content,recv_addr = udp_socket.recvfrom(1024)
	print("%s:%s"%(recv_addr,(recv_content.decode("utf-8"))))