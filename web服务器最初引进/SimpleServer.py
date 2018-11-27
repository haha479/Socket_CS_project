import socket
import sys
import gevent
import re
from gevent import socket,monkey
monkey.patch_all()

class SimpleServer(object):
	def __init__(self,app):
		self.web_Tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.app = app
		self.response_headers = ""
	def bind(self,port):
		self.web_Tcp.bind(("",port))
	#这个方法用来获得返回给浏览器的响应行和头
	def start_response(self,statu,header):

		#响应行
		response_line = "HTTP 1.1" + statu + "\r\n"

		response_header = ""
		for head in header :
			response_header += "%s: %s\r\n"%head
		#响应行和响应头拼串
		self.response_headers = response_line + response_header
	def recv_send(self,client_socket,client_addr):
		recv_data = client_socket.recv(1024)
		print("%s: \n%s"%(str(client_addr),recv_data.decode("utf-8")))

		#获得浏览器请求的第一行GET /index.html HTTP/1.1
		recv_start_line = recv_data.splitlines()[0]

		#通过正则获得浏览器请求的文件路径
		file_path = re.match(r"\w+ +(/\w*[^ ]*) ",recv_start_line.decode("utf-8")).group(1)

		print("文件名==%s"%file_path)
		#定义一个字典来放浏览器的一些请求信息路径
		env = {
			"PATH_INFO": file_path
		}

		#编码
		response_code = "Content-Type:text/html;Charset=utf-8\r\n"

		#返回给浏览器的响应体
		response_body = self.app(env,self.start_response)
		print("---==%s"%response_body)
		#返回给浏览器的所有数据
		response_data = self.response_headers + response_code + "\r\n" + response_body

		print("response_data==%s"%response_data)
		client_socket.send(response_data.encode("utf-8"))
		client_socket.close()
	def start(self):
		self.web_Tcp.listen(128)

		while True :
			client_socket,client_addr = self.web_Tcp.accept()
			gevent.spawn(self.recv_send,client_socket,client_addr)

if __name__ == '__main__':

	argvs = sys.argv[1]

	#获得模块名
	module_name,add_name = argvs.split(":")

	#动态的导入模块
	m = __import__(module_name)

	#得到simpleFrame中的实例对象app
	app = getattr(m,add_name)

	#创建simpleServer的实例对象,并将app传入
	simpleserver = SimpleServer(app)

	simpleserver.bind(9090)

	simpleserver.start()

