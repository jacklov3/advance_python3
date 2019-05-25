#-*- coding:utf-8 -*-
'''
线程池
'''

from concurrent.futures import ThreadPoolExecutor
import threading
import time

#定义一个准备作为线程任务的函数

def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name+' '+str(i))
        my_sum +=1
    return my_sum

# #创建一个包含2条线程的线程池
# pool = ThreadPoolExecutor(max_workers=2)
# #向线程池提交一个task，50会作为action函数的参数
# future1 = pool.submit(action,50)
# future2 = pool.submit(action,100)
#
# #判断future1代表的任务是否结束
# print(future1.done())
# time.sleep(3)
#
# print(future2.done())
# print(future1.result())
# print(future2.result())
# #关闭线程池
# pool.shutdown()


# 使用回调函数重写上面的阻塞式代码

with ThreadPoolExecutor(max_workers=2) as pool:
    #提交一个任务,50作为函数的参数
    future1 = pool.submit(action,50)
    #再提交一个task,
    future2 = pool.submit(action,100)
    def get_result(future):
        print(future.result())
    future1.add_done_callback(get_result)
    future2.add_done_callback(get_result)
    print('-----------------')