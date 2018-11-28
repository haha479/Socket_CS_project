import socket

#创建socket

udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#创建的飞秋用户信息
#飞秋格式,1:12312312312:用户名:电脑名称-pc:程序的操作位(32):"发送内容".encode("gb2312"),ip地址,端口
info = "1:12312312312:我叫哈哈:小霸王-pc:32:you illiteracy".encode("gb2312")
#创建要发送到的电脑信息
address = ("192.168.16.90",2425)

#发送
udp_socket.sendto(info,address)

#关闭
udp_socket.close()