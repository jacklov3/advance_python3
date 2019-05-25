#-*-coding:utf-8-*-
'''
使用线程池的map函数
'''
from concurrent.futures import ThreadPoolExecutor
import threading
import time

#定义一个准备作为线程任务的函数

def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name+' '+str(i))
        my_sum +=i
    return my_sum
#创建一个包含4条线程的线程池
with ThreadPoolExecutor(max_workers=4) as pool:
    #启动3个线程
    results = pool.map(action,(50,100,150))
    print('--------------')
    for r in  results:
        print(r)