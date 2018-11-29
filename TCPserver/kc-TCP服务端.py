import socket
import threading
#利用多线程,能接能收

#接收客户端发过来的消息
def recv_data(new_socket):
	for x in range(5):
		# 打印从客户端发过来的请求
		client_data = new_socket.recv(1024)
		print(client_data.decode("utf-8"))

#回应客户端
def send_data(new_socket):
	for x in range(5):
		#发送回应给客户端
		send_info = input("<<:")
		new_socket.send(send_info.encode("utf-8"))

def main():
	#创建套接字
	tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	#绑定地址
	server_addr = ("",6789)
	tcp_socket.bind(server_addr)

	#监听状态
	tcp_socket.listen(3)

	#阻塞状态,被动等待
	print("server already open")
	new_socket ,client_addr = tcp_socket.accept()

	# print(client_addr)
	#创建两个线程
	tr = threading.Thread(target=recv_data,args=(new_socket,))
	ts = threading.Thread(target=send_data,args=(new_socket,))

	tr.start()
	ts.start()

	tr.join()
	ts.join()
	#关闭套接字
	new_socket.close()
	tcp_socket.close()

if __name__ == '__main__':
	main()