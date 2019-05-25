#-*-coding:utf-8-*-

import multiprocessing
import time
import os
#
# def action(name='default'):
#     print('(%s)进程正在执行，参数为：%s'%(os.getpid(),name))
#     time.sleep(3)
#
# if __name__=='__main__':
#     #创建包含4条进程的进程池
#     pool = multiprocessing.Pool(processes=4)
#     pool.apply_async(action)
#     pool.apply_async(action,args=('位置参数',))
#     pool.apply_async(action,kwds={'name':'关键字参数'})
#     pool.close()
#     pool.join()

def action(max):
    my_sum=0
    for i in range(max):
        print('(%s)进程正在执行:%d'%(os.getpid(),i))
        my_sum +=i
    return my_sum

if __name__=='__main__':
    #创建一个包含4条进程的进程池
    with multiprocessing.Pool(processes=4) as pool:
        #使用map创建3个进程
        results = pool.map(action,(50,100,150))
        print('----------')
        for r in results:
            print(r)
