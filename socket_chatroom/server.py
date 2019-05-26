#-*- coding:utf-8-*-

import socket
import threading
#定义保存所有socket的列表

socket_list = []
#创建socket对象
ss = socket.socket()
#将socket绑定到本机IP和端口
ss.bind(('127.0.0.1',30000))
#服务端开始监听来自客户端的连接
ss.listen()

def read_from_client(s):
    try:
        return s.recv(2048).decode('utf-8')
    #如果捕获到异常，则表示该socket对应的客户端已经关闭
    except:
        socket_list.remove(s)

def server_target(s,addr):
    try:
        #循环不断从socket中读取客户端发送过来的数据
        while True:
            content = read_from_client(s)
            print(content)
            if content is None:
                break
            for client_s in socket_list:
                if client_s is not s:
                    client_s.send((str(addr)+'： '+content).encode('utf-8'))
    except Exception as e:
        print(e)

while True:
    #阻塞，等待连接
    s,addr = ss.accept()
    socket_list.append(s)
    #每当客户端连接后启动一个线程为该客户端服务
    threading.Thread(target=server_target,args=(s,addr)).start()

