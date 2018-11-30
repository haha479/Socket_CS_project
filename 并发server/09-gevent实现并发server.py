import gevent
from gevent import socket,monkey
monkey.patch_all()#动态的把系统socket换成gevent中的socket
def recv_data(client_socket,client_addr):
	while True :
		recv_info = client_socket.recv(1024)
		#如果客户端发送了请求就打印
		if recv_info:
			print("客户端:%s 请求:%s"%(str(client_addr),recv_info.decode("gb2312")))
		#没有发送就关闭套接字并退出循环
		else :
			client_socket.close()
			break
def main():
	#创建套接字
	s = socket.socket()

	#绑定地址
	s.bind(("",6789))

	#监听状态
	s.listen(1000)

	while True :
		#被动等请求
		client_socket,client_addr = s.accept()

		gevent.spawn(recv_data,client_socket,client_addr)

if __name__ == '__main__':
	main()