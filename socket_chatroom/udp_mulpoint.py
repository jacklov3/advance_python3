#-*- coding:utf-8-*-
'''
    udp多点广播实现聊天室应用
'''

import time
import socket
import threading
import os

#定义本机地址
SENDERIP = '127.0.0.1'
#定义本地端口
SENDERPROT = 30000
#定义本程序的多点广播IP地址
MYGROUP = '230.0.0.1'
#用过type属性创建基于UDP协议的socket
s = socket.socket(type=socket.SOCK_DGRAM)
#将该socket绑定到0.0.0.0的虚拟IP
s.bind(('0.0.0.0',SENDERPROT))
#设置广播消息的TTL
s.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,64)
#设置允许多点广播使用相同的端口
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#将socket加入广播组
status = s.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,socket.inet_aton(MYGROUP)+socket.inet_aton(SENDERIP))
#定义从socket读取数据的方法
def read_socket(sock):
    while True:
        data = sock.recv(2048)
        print('信息:',data.decode('utf-8'))
threading.Thread(target=read_socket,args=(s,)).start()
while True:
    line = input('')
    if line is None or line == 'exit':
        break
        os._exit(0)
    s.sendto(line.encode('utf-8'),(MYGROUP,SENDERPROT))
