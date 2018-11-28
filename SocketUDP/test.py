import threading
import socket
import time
#接收信息
def recvData():
	while True :
		recv_data = udp_socket.recvfrom(1024)
		# print(recv_data)
		#打印接收的信息
		print("用户:%s , content:%s"%(recv_data[1],recv_data[0].decode("gb2312")))

#发送信息
def sendData():
	while True:
		send_info = input("<<")

		udp_socket.sendto(send_info.encode("gb2312"),(des_ip,des_port))


udp_socket = None

des_ip = ""

des_port = 0

def main():
	global udp_socket

	global des_ip

	global des_port
	udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	#绑定端口
	udp_socket.bind(("",4124))

	des_ip = input("输入发送到的IP:")
	des_port = int(input("输入发送到的端口:"))

	tr = threading.Thread(target=recvData)
	ts = threading.Thread(target=sendData)

	tr.start()

	ts.start()

	tr.join()

	ts.join()

if __name__ == '__main__':
	main()