import socket
from threading import Thread

def recv_send(client_socket,client_addr):
	recv_data = client_socket.recv(1024)

	print("%s:\n%s"%(str(client_addr),recv_data.decode("utf-8")))

	#按照HTTP的格式封装数据给客户端
	#响应行（状态）
	response_start_line = "HTTP/1.1 200 OK\r\n"
	#响应头
	response_headers = "Serverha:bin_server\r\n"
	#告诉客户端编码方式
	response_code = "Content-Type: text/html;Charset=utf-8\r\n"
	#空行
	response_blank = "\r\n"
	#响应体
	response_body = "欢迎光临,客观里边请"
	#拼串
	response_data = response_start_line+response_headers+response_code+response_blank+response_body

	#发送内容给客户端
	client_socket.send(response_data.encode("utf-8"))

	#关闭服务器
	client_socket.close()
def main():

	#创建套接字
	tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	tcp_socket.bind(("",8989))

	tcp_socket.listen(128)

	while True :
		client_socket,client_addr = tcp_socket.accept()

		t1 = Thread(target=recv_send,args=(client_socket,client_addr))

		t1.start()
if __name__ == '__main__':
	main()