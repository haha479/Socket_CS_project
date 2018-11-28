import socket

#创建socket
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#绑定端口
udp_socket.bind(("",7777))

#使用socket接受内容
recv_data = udp_socket.recvfrom(1024)#1024表示本次接受的最大字节数

#如果是中文就需要编译(接受的是网络助手发过来的信息,所以需要用gb2312编译)
new_recv_data = recv_data[0].decode("gb2312")
print(recv_data)
print(new_recv_data)
udp_socket.close()

