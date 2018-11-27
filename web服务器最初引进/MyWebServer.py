import socket
import re
import sys
import gevent
from gevent import socket,monkey
monkey.patch_all()

#静态变量
HTTP_PATH = "./html"
#
HTTP_WSGI_DIR = "./wsgi"
class HttpServer(object):
	def __init__(self,app):
		self.web_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.app = app
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

	#用于得到浏览器请求的数据,和发送响应给浏览器
	def recv_send(self,client_socket, client_addr):
		# 打印从客户端发过来的请求,并且有换行
		recv_data = client_socket.recv(1024)
		print("%s:\n%s" % (str(client_addr), recv_data.decode("utf-8")))

		# 得到网络信息的第一行,里面有包含源文件的位置
		info_line = recv_data.splitlines()[0]

		# 利用正则得到源文件路径名
		file_path = re.match(r"\w+ +(/\w*[^ ]*) ", info_line.decode("utf-8")).group(1)
		print("文件名===%s"%file_path)
		#利用正则得到用户的请求方式,GET或POST
		method = re.match(r"(\w+)\s+/\w*[^ ]* ", info_line.decode("utf-8")).group(1)

		#定义一个字典,用于装从用户请求信息中截取的信息
		#path_info:文件的路径
		#math: 请求方式
		env = {"PATH_INFO": file_path,
			   "MATH": method
			   }


		#self.app是框架里面的的Applicatoion类的实例对象,下面这步等于是调用了call方法
		#call方法中返回的结果就会赋值给响应体
		response_body = self.app(env,self.start_response)

		print("====%s"%response_body)
		#最终返回给浏览器的数据就是响应行头和响应体拼串
		response_data = self.response_headers + "\r\n" + response_body

		#返回给浏览器信息
		client_socket.send(response_data.encode("utf-8"))
		client_socket.close()
def main():
	#动态的将模块添加到最靠前
	sys.path.insert(1,HTTP_WSGI_DIR)

	#在运行的时候:python MyWebServer.py MyWebFrame:Application
	#得到argvs = MyWebFrame:Application
	argvs = sys.argv[1]

	#将MyWebFrame:Application切片
	mudole_name,app_name = argvs.split(":")

	#动态的导入模块
	m = __import__(mudole_name)

	#使用getattr(加载模块的属性或类)
	#app就是Application实例化好的对象,并且传入了路由信息
	app = getattr(m,app_name)

	http_server = HttpServer(app)
	http_server.bind(8900)
	http_server.start()

if __name__ == '__main__':
	main()