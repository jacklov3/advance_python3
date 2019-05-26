#-*-coding:utf-8-*-
'''
    socket简单的服务端
'''
import socket

#创建socket对象
s = socket.socket()
#绑定地址和端口号
s.bind(('127.0.0.1',30000))
#开始监听来自客户端的连接
s.listen()
while True:
    #收到客户端socket请求时，该方法返回对应的socket和远程地址
    c,addr = s.accept()
    print(c)
    print('连接地址:',addr)
    c.send('您好，收到了您的连接,祝您生活愉快!'.encode('utf-8'))
    #关闭连接
    c.close()