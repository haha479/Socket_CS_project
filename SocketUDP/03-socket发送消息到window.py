import socket

#创建socket-udp

udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#要发送到的电脑ip和端口信息(本机电脑IP和网络助手的端口)
sendaddress = ("192.168.16.90",6665)

#网络助手默认是用gb2312解码,所以需要用到encode函数解码
msg = "哈哈".encode("gb2312")

#发送信息
udp_socket.sendto(msg,sendaddress)

#关闭
udp_socket.close()

