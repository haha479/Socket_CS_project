import time
#将返回给浏览器的数据解耦到次脚本文件中


def get_time(env,start_response):
	statu = "200 OK"
	headers = [('Content-Type', 'text/html')]
	start_response(statu,headers)
	return time.ctime()

def get_love(env,start_response):
	statu = "200 OK"
	headers = [('Content-Type', 'text/html')]
	start_response(statu,headers)
	return "Love"
