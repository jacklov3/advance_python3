#-*- coding:utf-8-*-

import  threading

#定义准备作为线程执行体的action函数

def action(max):
    for i in range(max):
        print(threading.current_thread().name+' '+str(i))

for i in range(100):
    print(threading.current_thread().name+' '+str(i))
    if i == 20:
        threading.Thread(target=action,args=(100,)).run()
        threading.Thread(target=action,args=(100,)).run()
        