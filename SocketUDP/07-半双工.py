import socket
import time
#同一个套间字，可以发送和接收
#使用socket创建发送方
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#绑定发送的端口
# udp_socket.bind(("",2222))

send_content = input("请输入发送的信息:")

#发送的内容
send_content = send_content.encode("gb2312")

#发送到的电脑信息
send_address = ("192.168.1.151",4134)

#发送
udp_socket.sendto(send_content,send_address)


#获取接受的信息并解码打印
recv_content = udp_socket.recvfrom(1024)
new_recv_content = recv_content[0].decode("gb2312")

print("从网络助手接收到的数据:%s"%(new_recv_content))

#关闭套间字
udp_socket.close()