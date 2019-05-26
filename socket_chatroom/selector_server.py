#-*- coding:utf-8-*-
import selectors,socket

#创建默认的selectors对象
sel = selectors.DefaultSelector()
#负责监听'有数据可读'事件的函数

def read(skt,mask):
    try:
        #读取数据
        data = skt.recv(1024)
        if data:
            for s in socket_list:
                s.send(data)
        else:
            print('关闭',skt)
            sel.unregister(skt)
            skt.close()
            socket_list.remove(skt)
    except:
        print('关闭',skt)
        sel.unregister(skt)
        skt.close()
        socket_list.remove(skt)
socket_list=[]

#负责监听"客户连接进来"事件的函数
def accept(sock,mask):
    conn,addr = sock.accept()
    #使用socket_list保存代表客户端的socket
    socket_list.append(conn)
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)
sock = socket.socket()
sock.bind(('127.0.0.1',30000))
sock.listen()
#设置该socket是非柱塞式的
sock.setblocking(False)
#注册事件监听函数
sel.register(sock,selectors.EVENT_READ,accept)
#循环提取sel的事件
while True:
    events = sel.select()
    for key,mask in events:
        #key的data属性获取该事件注册的监听函数
        callback = key.data
        #调用监听函数，key的fileobj属性获取被监听的socket对象
        callback(key.fileobj,mask)