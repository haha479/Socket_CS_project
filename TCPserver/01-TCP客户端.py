import socket

#创建套接字
client_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 与服务器建立链接
server_addr = ("192.168.16.90", 5657)
client_tcp.connect(server_addr)

for i in range(5):
	send_info = input("发送到服务端的info:")
	client_tcp.send(send_info.encode("utf-8"))

	#打印服务器回应的内容
	recv_info = client_tcp.recv(1024)
	print(recv_info.decode("utf-8"))

client_tcp.close()