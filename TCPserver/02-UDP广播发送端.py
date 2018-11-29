import socket

#创建套间字
udp_broadcast = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_broadcast.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

for x in range(100):
	#发送消息
	send_content = input("发送的广播内容:")
	# udp_broadcast.sendto(send_content.encode("utf-8"),("<broadcast>",8080))
	#网络调试助手专用编码(gb2312)
	udp_broadcast.sendto(send_content.encode("utf-8"), ("<broadcast>", 8080))
udp_broadcast.close()
