#-*-coding:utf-8-*-
'''
    多进程编程
'''

import multiprocessing
import os
#
# #定义进程执行体
#
# def action(max):
#     for i in range(max):
#         print('(%s)子进程 (父进程:(%s)):%d'%(os.getpid(),os.getppid(),i))
#
# if __name__=='__main__':
#     #主进程
#     for i in range(100):
#         print('(%s)主进程:%d'%(os.getpid(),i))
#         if i == 20:
#             #创建、启动进程
#             mp1 = multiprocessing.Process(target=action,args=(100,))
#             mp1.start()
#             #创建并启动另一个进程
#             mp2 = multiprocessing.Process(target=action,args=(100,))
#             mp2.start()
#             mp2.join()
#     print('主进程执行完成!')


# 第二种方法，通过继承Process类来创建子进程

class MyProcess(multiprocessing.Process):
    def __init__(self,max):
        self.max=max
        super().__init__()

    #重写run方法
    def run(self):
        for i in range(self.max):
            print("(%s)子进程 (父进程:(%s)):%d"%(os.getpid(),os.getppid(),i))

if __name__=='__main__':
    #主程序
    for i in range(100):
        print('(%s)主进程:%d'%(os.getpid(),i))
        if i==20:
            #创建一个进程实例
            mp1 = MyProcess(100)
            mp1.start()

            #创建另一个进程实例
            mp2 = MyProcess(100)
            mp2.start()
            mp2.join()
    print('主进程执行完成!')
