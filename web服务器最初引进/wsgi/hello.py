import time


#得到系统时间
def get_ctime():
	return "hello"

#第一个参数是web服务器的相关信息,是一字典env
#第二个参数start_response是函数，用于封装响应行和响应头共两部分
#这个函数最终返回响应体
def application(env,start_response):
	statu = "200 OK"#代表执行get_ctime成功
	headers = [('Content-Type', 'text/html')]
	start_response(statu,headers)
	return get_ctime()