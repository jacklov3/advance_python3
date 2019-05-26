#-*-coding:utf-8-*-
'''
    简单的socket客户端
'''

import socket

#创建一个客户端socket
s = socket.socket()
#连接
s.connect(('127.0.0.1',30000))
print('---%s---'%s.recv(1024).decode('utf-8'))
s.close()