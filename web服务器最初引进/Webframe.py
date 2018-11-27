from WebServer import HttpServer

#静态变量
HTTP_PATH = "./html"

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
		#返回赋值给响应体
		return file_content.decode("utf-8")

def get_love(env,start_response):
	line = "200 OK"
	headers = [('Content-Type', 'text/html')]
	start_response(line,headers)
	return "love!!!"

class Application(object):
	def __init__(self,urls):
		self.urls = urls
	def __call__(self,env,start_response):
		file_name = env.get("PATH_INFO","/")

		#将框架中的函数信息遍历
		for url,function in self.urls :
			#如果这些函数中包含用户输入的函数
			if url == file_name :
				#返回这个函数,返回的值赋值给响应体
				return function(env,start_response)

		#如果上面出错了,则执行下面
		statu = "404 Not Found\r\n"

		headers = [
			("Content-Type", "Text/plain")

		]
		#调用start_response方法
		start_response(statu,headers)

		return "Not Found Sorry !!"

if __name__ == '__main__':

	#定义一个列表用来装框架中的所有可执行函数
	urls = [
		("/love",get_love),
		("/index.html",html_demo)
			]

	#创建Application的实例对象
	app = Application(urls)

	#创建服务器中HttpServer的实例对象
	httpserver = HttpServer(app)

	#调用HttpServer的绑定方法
	httpserver.bind(5678)

	#调用start方法来等待浏览器用户的进入
	httpserver.start()