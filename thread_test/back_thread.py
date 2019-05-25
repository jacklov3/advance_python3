#-*-coding:utf-8-*-

import threading

#定义后台线程的线程执行体与普通线程没有任何区别
def action(max):
    for i in range(max):
        print(threading.current_thread().name+' '+str(i))

t = threading.Thread(target=action,args=(100,),name= '后台线程')
#设置此线程为后台线程
t.daemon = True
#启动后台线程
t.start()
for i in range(10):
    print(threading.current_thread().name+' '+str(i))
