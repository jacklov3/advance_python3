#-*- coding:utf-8-*-

import threading

def action(max):
    for i in range(100):
        print(threading.current_thread().name+' '+str(i))

sd = threading.Thread(target=action,args=(100,))
for i in range(300):
    print(threading.current_thread().name+' '+str(i))
    if i ==20:
        #启动线程
        sd.start()
        print(sd.is_alive())
    if i>20 and not (sd.is_alive()):
        sd.start()