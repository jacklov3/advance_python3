#-*-coding:utf-8-*-
'''
    使用fork函数创建新进程,fork()函数后面的代码会被父进程和子进程分别执行，通过判断pid==0可以为子进程
    定义不同的函数
'''

import  os

print('父进程(%s)开始执行'% os.getpid())
#开始fork一个子进程

pid = os.fork()
print('进程进入:%s'%os.getpid())

#如果pid为0，表明子进程
if pid == 0:
    print('子进程，其ID为(%s)，父进程ID为(%s)'%(os.getpid(),os.getppid()))
else:
    print('我(%s)创建的子进程ID为(%s).'%(os.getpid(),pid))
print('进程结束:%s'%os.getpid())

