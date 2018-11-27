import socket
import re
import gevent
from gevent import socket,monkey
monkey.patch_all()

class WebServer(object):
	def __init__(self,app):
		self.web_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.app = app

	def bind(self,port):
		self.web_tcp.bind(("",port))

	def start_response(self,start,header):
		respones_start = "HTTP 1.1" + start + "\r\n"

		response_head = ""

		for head in header :
			response_head += "%s :%s \r\n" %head

			#最终得到的就是响应行和响应头
			self.response_headers = respones_start + response_head

	def recv_send(self,client_socket ,client_addr):
		#获取从浏览器发过来的信息并打印
		recv_data = client_socket.recv(1024)
		print("%s: \n%s"%(str(client_addr),recv_data.decode("utf-8")))

		#第一行的信息
		start_line = recv_data.splitlines()[0]

		#利用正则得到请求函数名
		file_path = re.match(r"\w+ +(/\w*[^ ]*) ", start_line.decode("utf-8")).group(1)

		#利用正则来获取请求的方式
		method = re.match(r"(\w+)\s+/\w*[^ ]* ", start_line.decode("utf-8")).group(1)

		#定义一个字典来放请求的函数名和请求方式
		env = {
			"PATH_INFO":file_path,
			"METHOD":method
		}

		#获取响应体
		response_body = self.app(env,self.start_response)

		#将响应行响应头和响应体拼串起来
		response_data = self.response_headers + "\r\n" + response_body

		#发送给浏览器数据
		client_socket.send(response_data.encode("utf-8"))
		client_socket.close()
	def start(self):
		self.web_tcp.listen(128)

		while True :
			client_socket ,client_addr = self.web_tcp.accept()

			#创建协程
			gevent.spawn(self.recv_send,client_socket ,client_addr)
