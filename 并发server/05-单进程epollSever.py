from socket import *
import select

#创建套接字
tcp_server = socket(AF_INET,SOCK_STREAM)
#绑定地址
tcp_server.bind(("",7890))
#监听模式
tcp_server.listen(5)
#得到epoll对象
ep = select.epoll()
ep.register(tcp_server.fileno())
