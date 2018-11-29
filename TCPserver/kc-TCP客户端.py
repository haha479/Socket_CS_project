import socket
import threading

#接收服务器回应的数据
def recv_data(tcp_socket):
	for i in range(5):
		# 接收到从服务器回应的数据并打印
		recv_data = tcp_socket.recv(1024)
		print(recv_data.decode("utf-8"))

#往服务器发送数据
def send_data(tcp_socket):
	for k in range(5):
		# 发送数据到服务器
		send_info = input("到服务器:")
		tcp_socket.send(send_info.encode("utf-8"))

def main():
	#创建套接字
	tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	#与服务器建立链接
	server_addr = ("192.168.16.90",6789)
	tcp_socket.connect(server_addr)

	# 创建线程
	tr = threading.Thread(target=recv_data, args=(tcp_socket,))
	ts = threading.Thread(target=send_data,args=(tcp_socket,))

	tr.start()
	ts.start()

	tr.join()
	ts.join()


	#关闭套接字
	tcp_socket.close()

if __name__ == '__main__':
	main()