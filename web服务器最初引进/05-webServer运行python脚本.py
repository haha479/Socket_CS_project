import socket
import re
import sys
import gevent
from gevent import socket,monkey
monkey.patch_all()

#静态变量
HTTP_PATH = "./html"
#
HTTP_mpodul_path = "./wsgi"
class HttpServer(object):
	def __init__(self):
		self.web_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	def bind(self,port):
		self.web_tcp.bind(("", port))
	#用户等待浏览器链接
	def start(self):
		self.web_tcp.listen(128)
		while True:
			client_socket, client_addr = self.web_tcp.accept()
			# 有客户端进来就创建协程
			gevent.spawn(self.recv_send, client_socket, client_addr)

	#用于封装响应行和响应头
	def start_response(self,statu,headers):
		response_start_line = "HTTP 1.1 " + statu + "\r\n"

		#响应头
		response_header = ""

		for header in headers :
			response_header += "%s: %s\r\n" % header

			#最终得到self.response_headers这个数据就是响应行和响应头
			self.response_headers = response_start_line + response_header

	#用于发送和接受数据
	def recv_send(self,client_socket, client_addr):
		# 打印从客户端发过来的请求
		recv_data = client_socket.recv(1024)
		print("%s:\n%s" % (str(client_addr), recv_data.decode("utf-8")))
		# 得到网络信息的第一行,里面有包含源文件的位置
		info_line = recv_data.splitlines()[0]
		# print(info_line)
		#b'GET /ctime.py HTTP/1.1'
		# 利用正则得到源文件路径
		file_path = re.match(r"\w+ +(/\w*[^ ]*) ", info_line.decode("utf-8")).group(1)
		# print("one line == %s"%file_path).
		# print(file_path)
		#如果用户输入的地址是以py结尾的（运行python脚本）
		if file_path.endswith(".py"):
			try :
				#取到的路径名就是模块名
				m = __import__(file_path[1:-3])
			except :
				# 如果出错就回复文件不在
				# 响应行
				response_start_line = "HTTP 1.1 404 Not Found\r\n"
				# 响应头
				response_header = "Server bin_haha\r\n"
				# 告诉浏览器解码方式
				response_code = "Content-Type:text/html;Charset=utf-8\r\n"
				# 空白行
				response_blank = "\r\n"
				# 响应体
				response_body = "访问的文件不存在!请核对路径谢谢"
				response_data = response_start_line + response_header + response_code + response_blank + response_body
			else :
				# time = m.get_time()
				# print("time==%s"%time)
				env = {}
				#调用m模块里面的application函数,这个函数返回的是一个响应体
				response_body = m.application(env,self.start_response)
				#最终返回给浏览器的数据就是响应行头和响应体拼串
				response_data = self.response_headers + "\r\n" + response_body


		else :
			#如果地址内没有输入文件名,只是输入了/就将其改为指定的文件名
			if "/" == file_path:
				file_path = "/index.html"
			try:
				f = open(HTTP_PATH + file_path, "rb")
			except:
				#如果出错就回复文件不在
				# 响应行
				response_start_line = "HTTP 1.1 404 Not Found\r\n"
				# 响应头
				response_header = "Server bin_haha\r\n"
				# 告诉浏览器解码方式
				response_code = "Content-Type:text/html;Charset=utf-8\r\n"
				# 空白行
				response_blank = "\r\n"
				# 响应体
				response_body = "访问的页面不存在!"
			else:

				file_content = f.read()

				# 响应行
				response_start_line = "HTTP 1.1 200 OK\r\n"
				# 响应头
				response_header = "Server bin_haha\r\n"
				# 告诉浏览器解码方式
				response_code = "Content-Type:text/html;Charset=utf-8\r\n"
				# 空白行
				response_blank = "\r\n"
				# 响应体
				response_body = file_content.decode("utf-8")

			# 将所有的数据拼串成总的发送给浏览器的数据
			response_data = response_start_line + response_header + response_code + response_blank + response_body
		#返回给浏览器信息
		client_socket.send(response_data.encode("utf-8"))
		client_socket.close()
def main():
	#动态的将模块添加到最靠前
	sys.path.insert(1,HTTP_mpodul_path)
	h = HttpServer()
	h.bind(8900)
	h.start()

if __name__ == '__main__':
	main()