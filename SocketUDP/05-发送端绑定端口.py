import socket
# 每发送一次就关闭掉了进程
# 就会导致每次发送到另一台电脑上显示的不是同一个端口号
# 因为动态端口是随机赋予的
# 可以绑定一个固定的端口
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#绑定发送端的端口
#两个参数用一定用括号括起来,第一个参数是IP,不写就会取本机ip
#当主机有多个网卡就会有多个ip
#第二个是绑定的端口
udp_socket.bind(("",6666))

#发送的内容
send_content = "哈哈我是发送的内容".encode("gb2312")

#发送到的电脑信息
send_address = ("192.168.16.90",6665)

#发送
udp_socket.sendto(send_content,send_address)
#关闭
udp_socket.close()