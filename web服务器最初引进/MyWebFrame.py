import time
#将返回给浏览器的数据解耦到次脚本文件中
import sys
# from MyWebServer import HttpServer

#静态变量
HTTP_PATH = "./html"
#
HTTP_WSGI_DIR = "./wsgi"

def html_demo(env,start_response):
	#响应行头
	statu = "200 OK"
	headers = [('Content-Type', 'text/html')]
	start_response(statu, headers)

	file_name = env.get("PATH_INFO", "/")
	try:
		f = open(HTTP_PATH + file_name, "rb")
	except:
		# 如果出错就回复文件不在
		return "文件不存在!!!"
	else:
		file_content = f.read()
		return file_content.decode("utf-8")
#网页中出现hello!!
def say_hello(env,start_response):
	statu = "200 OK"
	headers = [('Content-Type', 'text/html')]
	start_response(statu,headers)
	#返回的赋值给响应体
	return "hello !!"

def get_time(env,start_response):
	statu = "200 OK"
	headers = [('Content-Type', 'text/html')]
	start_response(statu,headers)
	# 返回的赋值给响应体
	return time.ctime()

def get_love(env,start_response):
	statu = "200 OK"
	headers = [('Content-Type', 'text/html')]
	start_response(statu,headers)
	# 返回的赋值给响应体
	return "Love !"

#这个类用来跟服务器交互
class Application(object):
	def __init__(self,urls):
		self.urls = urls

	def __call__(self,env,start_response):
		file_name = env.get("PATH_INFO","/")
		#便利这个框架中的路由
		for url,function in self.urls :
			#如果路由中有一个函数是用户访问的
			if file_name == url :
				#返回的值就是这个代码中的函数返回值,最终赋值给响应体
				info = function(env,start_response)
				return	info

		#如果上面错误了,没有找到对应的函数,则会执行下面的代码
		#响应状态
		statu = "404 Not Found"
		# 2.响应头信息
		headers = [
			("Content-Type", "Text/plain")

		]
		# 生成响应头
		start_response(statu, headers)
		# 返回响应体内容
		return "Not Found,Sorry!++"
#定义列表存放框架中的所有可执行函数(也称路由)--成为了Application的静态属性
urls = [("/",get_time),
		("/love",get_love),
		("/hello",say_hello),
		("/index.html",html_demo)

		]
#实例化框架内的对象
app = Application(urls)
# if __name__ == '__main__':
# 	pass

	#
	# #实例化HttpServer对象
	# httpserver = HttpServer(app)
	#
	# #调用HttpServer中的绑定方法
	# httpserver.bind(5657)
	#
	# #调用HttpServer中的start方法开始监听等待客户请求
	# httpserver.start()
