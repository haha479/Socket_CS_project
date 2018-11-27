import socket
import gevent
from gevent import socket,monkey
monkey.patch_all()
import re

#写一个静态变量
ROOT_HTML = "./html"
def recv_send(client_socket,client_addr):
	#接受客户端的请求并打印
	recv_data = client_socket.recv(1024)
	print("%s:\n%s"%(str(client_addr),recv_data.decode("utf-8")))

	#得到客户端请求信息的第一行:GET /index.html HTTP/1.1
	request_start_line = recv_data.splitlines()[0].decode("utf-8")

	#使用正则得到网页源文件名
	file_name = re.match(r"\w+\s+(/\w*[^ ]*)",request_start_line).group(1)

	# print("filename == %s"%file_name)

	if "/" == file_name :
		file_name = "/index.html"
	try :
		#打开请求的源网页文件并且可读
		f = open(ROOT_HTML+file_name,"rb")
	except :
		# 响应行
		response_start_line = "HTTP/1.1 404 Not found\r\n"
		# 响应头
		response_header = "Server: zhoubinserver\r\nContent-Type:text/html;Charset=utf-8\r\n"
		# 空白行
		response_blank = "\r\n"
		# 响应体
		response_body = "访问的文件不存在!"
	else :

		file_content = f.read()
		#封装HTTP的格式发给客户端
		#响应行
		response_start_line = "HTTP/1.1 200 OK\r\n"
		#响应头
		response_header = "Server: zhoubinserver\r\nContent-Type:text/html;Charset=utf-8\r\n"
		#空白行
		response_blank = "\r\n"
		#响应体
		response_body = file_content.decode("utf-8")

	#拼串包装
	response_data = response_start_line+response_header+response_blank+response_body

	client_socket.send(response_data.encode("utf-8"))

	client_socket.close()
def main():

	tcp_web = socket.socket()

	tcp_web.bind(("",6789))

	tcp_web.listen(128)

	while True :
		client_socket,client_addr = tcp_web.accept()

		gevent.spawn(recv_send,client_socket,client_addr)


if __name__ == '__main__':
	main()