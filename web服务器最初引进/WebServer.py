import socket
import gevent
import re
from gevent import socket,monkey
monkey.patch_all()

class HttpServer(object):
	def __init__(self,app):
		self.http_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.app = app
	#绑定端口地址
	def bind(self,port):
		self.http_socket.bind(("",port))

	#这个方法用来封装响应头和行
	def start_response(self,line,headers):
		response_line = "HTTP 1.1" + line + "\r\n"

		response_header = ""
		for header in headers :
			response_header += "%s: %s\r\n" % header

			#最终得到响应行和响应头
			self.response_headers = response_line + response_header


	#这个函数用来接收浏览器的请求数据,和回复数据给浏览器
	def recv_send(self,client_socket,client_addr):
		#打印从浏览器发过来的请求并换行
		recv_client_data = client_socket.recv(1024)
		print("%s :\n%s"%(str(client_addr),recv_client_data.decode("utf-8")))

		#得到浏览器返回数据的第一行
		first_line = recv_client_data.splitlines()[0]

		#利用正则得到文件名
		file_path = re.match(r"\w+ +(/\w*[^ ]*) ",first_line.decode("utf-8")).group(1)

		#定义一个字典来装浏览器请求的信息
		env = {
			"PATH_INFO":file_path
		}

		#响应体 ---> 转到框架（执行框架中的__call__方法）
		response_body = self.app(env,self.start_response)

		#将响应行响应头和响应体拼串
		response_data = self.response_headers + "\r\n" + response_body
		#发送到浏览器的所有数据
		client_socket.send(response_data.encode("utf-8"))

		client_socket.close()

	#这个函数进入就开始等待浏览器的链接
	def start(self):
		self.http_socket.listen(128)

		while True :
			client_socket,client_addr = self.http_socket.accept()

			#创建协程
			gevent.spawn(self.recv_send,client_socket,client_addr)
