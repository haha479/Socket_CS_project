#coding=utf-8
import  socket
from multiprocessing import Process
from time import ctime
import re
#常量名字要大写
HTML_ROOT_DIR = "./html"
def handle_client(client_socket):
	#获取客户端请求的数据
	request_data = client_socket.recv(1024)
	request_lines = request_data.splitlines()
	for line in request_lines:
		print(line)
	#从b'GET /index.html HTTP/1.1或者b'GET / HTTP/1.1
	request_start_line = request_lines[0].decode("utf-8")
	# 使用正则表达式,得到请求路径/或者/index.html
	file_path = re.match(r"\w+ +(/[^ ]*)",request_start_line)
	file_name = file_path.group(1)
	print("file_name:",file_name)
	#因为HTML_ROOT_DIR = "./html"
	if "/" == file_name :
		file_name = "/index.html"
	try:
		#打开文件读取/html/index.html文件内容,以二进制方式
		f = open(HTML_ROOT_DIR+file_name,"rb")
	except:#文件没有找到返回404
		# 构造相应数据
		response_start_line = "HTTP/1.1 404 Found File\r\n"
		response_headers = "Server:My Server\r\n"
		response_body = "文件未找到，抱歉哦!"
	else:
		#文件存在，正常处理
		file_data = f.read()
		# 关闭文件
		f.close()
		#构造相应数据
		response_start_line = "HTTP/1.1 200 OK\r\n"
		response_headers = "Server:My Server\r\n"
		response_body = file_data.decode("utf-8")

	#拼接数据：注意响应头和响应体要加上\r\n
	response = response_start_line + response_headers+"\r\n"+response_body
	print("response data:",response)
	#client_socket.send(bytes(response,"utf-8"))
	client_socket.send(response.encode("utf-8"))
	client_socket.close()

def main():
	#创建TCP服务端
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#服务端口可以重复启动，不会被占用
	server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	#绑定端口
	server.bind(("",7788))
	#设置监听
	server.listen(128)

	while True:
		client_socket,client_address = server.accept()
		#print("[%s %s]客户已经链接上了"%(client_address[0],client_address[1]))
		print("[%s ]客户已经链接上了" % client_address)
		client = Process(target=handle_client,args=(client_socket,))
		client.start()
		# 在主进程中关闭链接
		client_socket.close()

if __name__ == "__main__":
	main()