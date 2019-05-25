#-*-coding:utf-8-*-

import sched,time
import threading

#定义线程调度器
s = sched.scheduler()
#定义被调度的函数

def print_time(name = 'default'):
    print('%s的时间：%s'%(name,time.ctime()))

print('主线程：',time.ctime())

#指定10秒之后执行print_time函数
s.enter(10,1,print_time)
#指定5秒之后执行print_time函数
s.enter(5,2,print_time,argument=('位置参数',))
s.enter(5,1,print_time,kwargs={'name':'关键字参数'})
s.run()
print('主线程:',time.ctime())