import socket
import threading
	#创建TCP服务器的步骤
	#1.创建套接字
	#2.绑定服务器的地址(IP和进程端口)
	#3.listen使套间字变为可以被动链接
	#4.accept等待客户端或用户链接
	#5.recv/send收发数据

#创建套接字
server_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定服务器地址
server_addr = ("",5657)
server_tcp.bind(server_addr)

#进入监听状态
server_tcp.listen(3)#最多允许三个客户端链接次服务器

#接收来自客户端的请求信息
def recv_data(new_socket,client_addr):
	for x in range(5):
		# 接收并打印打印从客户端发过来的请求
		recv_content = new_socket.recv(1024)
		print("%s发过来的信息:%s"%(client_addr,recv_content.decode("utf-8")))

#回应客户端
def send_data(new_socket):
	for i in range(5):
		#回应客户端
		send_info = input("回应客户端:")
		new_socket.send(send_info.encode("utf-8"))

def main():
# for i in range(5):
	new_socket,client_addr = server_tcp.accept()
# for x in range(5):

	#打印从客户端发过来的请求
	# recv_content = new_socket.recv(1024)
	# print(recv_content.decode("utf-8"))

	#创建两个线程
	tr = threading.Thread(target=recv_data,args=(new_socket,client_addr))
	ts = threading.Thread(target=send_data,args=(new_socket,))

	tr.start()
	ts.start()

	#回应客户端
	# send_info = input("<<")
	# new_socket.send(send_info)

	# new_socket.close()

if __name__ == '__main__':
	main()
server_tcp.close()
