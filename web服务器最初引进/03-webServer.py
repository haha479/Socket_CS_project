import socket
import re
import gevent
from gevent import socket,monkey
monkey.patch_all()

#静态变量
HTTP_PATH = "./html"

def recv_send(client_socket,client_addr):
	#打印从客户端发过来的请求
	recv_data = client_socket.recv(1024)
	print("%s:\n%s"%(str(client_addr),recv_data.decode("utf-8")))
	#得到网络信息的第一行,里面有包含源文件的位置
	info_line = recv_data.splitlines()[0].decode("utf-8")
	#利用正则得到源文件路径
	file_path = re.match(r"\w+\s+(/\w*[^ ]*)",info_line).group(1)
	# print("one line == %s"%file_path)

	if "/" == file_path :
		file_path = "/index.html"
	try :
		f = open(HTTP_PATH + file_path,"rb")
	except :
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
	else :

		file_content = f.read()

		#响应行
		response_start_line = "HTTP 1.1 200 OK\r\n"
		#响应头
		response_header = "Server bin_haha\r\n"
		#告诉浏览器解码方式
		response_code = "Content-Type:text/html;Charset=utf-8\r\n"
		#空白行
		response_blank = "\r\n"
		#响应体
		response_body = file_content.decode("utf-8")

	#拼川返回给客户端
	response_data = response_start_line + response_header + response_code + response_blank + response_body
	client_socket.send(response_data.encode("utf-8"))
	client_socket.close()
def main():
	web_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	web_tcp.bind(("",8908))
	web_tcp.listen(128)

	while True :
		client_socket,client_addr = web_tcp.accept()

		#有客户端进来就创建协程
		gevent.spawn(recv_send,client_socket,client_addr)

if __name__ == '__main__':
	main()