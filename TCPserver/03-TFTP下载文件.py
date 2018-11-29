import socket
import struct

udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

send_data = struct.pack("!H8sb5sb",1,"test.jpg",0,"octet",0)

#发送数据
udp_socket.sendto(send_data,("192.168.16.90",69))

udp_socket.close()
