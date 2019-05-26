#-*- coding:utf-8-*-

import selectors,socket,threading

#创建默认的selectors对象
sel = selectors.DefaultSelector()
#负责监听'有数据可读'事件的函数
def read(conn,mask):
    data = conn.recv(1024)
    if data:
        print(data.decode('utf-8'))
    else:
        print('closing',conn)
        sel.unregister(conn)
        conn.close()

#创建socket对象
s = socket.socket()
#连接远程主机
s.connect(('127.0.0.1',30000))
#设置该socket是非阻塞的
s.setblocking(False)
sel.register(s,selectors.EVENT_READ,read)
def keyboard_input(s):
    while True:
        line = input('')
        if line is None or line == 'exit':
            break
        s.send(line.encode('utf-8'))
#采用线程不断读取用户的键盘输入
threading.Thread(target=keyboard_input,args=(s,)).start()
while True:
    #获取事件
    events = sel.select()
    for key,mask in events:
        callback = key.data
        callback(key.fileobj,mask)
