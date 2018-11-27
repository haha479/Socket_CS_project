import time
from Server import WebServer

#静态变量,用来找到html文件的位置
HTTP_DEMO_PATH = "./html"

#静态网页
def html_demo(env,start_response):
	statu = "200 OK"
	header = [
		("Content-type", "Text-plain")
	]
	file_path = env.get("PATH_INFO","/")
	start_response(statu, header)
	try :
		f = open(HTTP_DEMO_PATH + file_path,"rb")
	except :

		return "Not Found Sorry"
	else :
		file_content = f.read()
		return file_content.decode("utf-8")

#打印时间
def get_time(env,start_response):
	statu = "200 OK"
	header = [
				("Content-type","Text-plain")
				  ]
	start_response(statu,header)
	#返回的值赋值给响应体
	return time.ctime()

#say hello
def get_hello(env,start_response):
	statu = "200 OK"
	header = [
				("Content-type","Text-plain")
				  ]
	start_response(statu,header)
	#返回的值赋值给响应体
	return "hello hahaa"

#跟服务器的接口
class Application(object):
	def __init__(self,urls):
		self.urls = urls

	def __call__(self,env,start_response):
		file_name = env.get("PATH_INFO","/")

		#便利这个框架中的函数信息
		for url,function in self.urls :

			#如果框架中有用户输入的函数
			if url == file_name :
				#返回的值赋值给响应体
				return function(env,start_response)

		#如果上面出错了
		statu = "404 Not Found"
		header = [
				("Content-type","Text-plain")
				  ]
		start_response(statu,header)
		#返回响应体
		return "Not Found Sorry"

#创建列表来放框架中的函数信息
urls = [("/time",get_time),
		("/hello",get_hello),
		("/index.html",html_demo)
		]

#创建Application的实例对象
app = Application(urls)

#创建WebServer的实例对象
webserver = WebServer(app)

#调用WebServer中的绑定函数
webserver.bind(8899)

#调用start方法等待浏览器响应
webserver.start()