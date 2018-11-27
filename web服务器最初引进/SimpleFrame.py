import time

#静态变量,用于打开指定的页面
HTTP_DEMO_PATH = "./html"

def get_time(env,start_response):
	statu = "200 OK"
	header = [("Content-Type", "Text/plain")]

	start_response(statu,header)

	#返回响应体
	return time.ctime()

def demo_html(env,start_response):
	file_path = env.get("PATH_INFO","/")
	header = [("Content-Type", "Text/plain")]
	try :
		f = open(HTTP_DEMO_PATH + file_path , "rb")

	except :
		statu = "404 Not Found"
		start_response(statu,header)
		#返回给响应体的值
		return "sorry ,Not Found !--"

	else :
		#如果访问的文件存在
		statu = "200 Ok"
		start_response(statu,header)
		file_content = f.read()
		#返回给响应体的值
		# print("==%s"%file_content.decode("utf-8"))
		return file_content.decode("utf-8")

class Applicaton(object):
	def __init__(self,urls):
		self.urls = urls

	def __call__(self,env,start_response):
		file_name = env.get("PATH_INFO","/")

		for url,func in self.urls :
			#如果框架中有跟用户请求相同的函数
			if url == file_name :
				func(env, start_response)
				#返回并且不执行下边的代码
				return func(env,start_response)

		#如果框架中没有用户输入的函数
		# statu = "404 Not Found++"
		# header = [("Content-Type", "Text/plain")]
		#
		# start_response(statu,header)
		#
		# return "Not Found so sorry"


#路由配置
urls = [
	("/time",get_time),
	("/index.html",demo_html)
		]

#创建实例对象
app= Applicaton(urls)