from socket import *
from multiprocessing import Process
#单进程服务器虽然可以允许多个客户端同时链接
#但不能同时服务与多个客户端
#下面写一个循环,每有一个客户端链接,就会创建一个子进程
#子进程函数,用于接受客户端数据
def recv_data(new_socket):
	while True :
		# 接收client数据并打印
		recv_data = new_socket.recv(1024)
		print(recv_data.decode("utf-8"))
	new_socket.close()
def main():
	#创建TCP套接字
	tcp_socket = socket(AF_INET,SOCK_STREAM)

	#绑定服务器地址
	server_addr = ("192.168.16.90",8890)
	tcp_socket.bind(server_addr)

	#进入监听状态
	tcp_socket.listen(5)
	while True :
		#阻塞状态,等待客户端请求,一旦请求则创建新的socket对象
		print("堵塞,等待新客户端请求~")
		new_socket,new_addr = tcp_socket.accept()

		#创建一个子进程
		p = Process(target=recv_data,args=(new_socket,))
		p.start()


	tcp_socket.close()

if __name__ == '__main__':
	main()