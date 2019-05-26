#-*- coding:utf-8-*-

import socket
import threading

#创建socket对象
s = socket.socket()
#连接远程主机

s.connect(('127.0.0.1',30000))

def read_from_server(s):
    while True:
        print(s.recv(2048).decode('utf-8'))

#客户端启动线程不断地读取来自服务器的数据
threading.Thread(target=read_from_server,args=(s,)).start()
while True:
    line = input('')
    if line is None or line == 'exit':
        break
    #将用户的键盘输入内容写入socket
    s.send(line.encode('utf-8'))
