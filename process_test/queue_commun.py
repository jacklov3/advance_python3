#-*- coding:-utf-8-*-
'''
    进程间通信的两种方式
'''

#队列通信
import multiprocessing
# def f(q):
#     print('(%s)进程开始放入数据...'%multiprocessing.current_process().pid)
#     q.put('Python')
#
# if __name__=='__main__':
#     #创建进程通信的Queue
#     q = multiprocessing.Queue()
#     #创建子进程
#     p = multiprocessing.Process(target=f,args=(q,))
#     #启动子进程
#     p.start()
#     print('(%s)进程开始取出数据...'%multiprocessing.current_process().pid)
#     #取出数据
#     print(q.get())
#     p.join()

# 管道通信

def f(conn):
    print('(%s)进程开始发送数据...'%multiprocessing.current_process().pid)
    #使用conn发送数据
    conn.send('python')

if __name__=='__main__':
    #创建Pipe,该函数返回两个pipeConnection对象
    parent_conn,child_conn = multiprocessing.Pipe()
    #创建子进程
    p = multiprocessing.Process(target=f,args=(child_conn,))
    p.start()
    print('(%s)进程开始接收数据...'%multiprocessing.current_process().pid)
    #通过conn读取数据
    print(parent_conn.recv())
    p.join()

