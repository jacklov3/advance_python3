#-*- coding:utf-8-*-

import queue

#定义一个长度为2的阻塞队列

bq = queue.Queue(2)
bq.put('Python')
bq.put('python')
print('1111111')
bq.put('Python')
print('2222222222')