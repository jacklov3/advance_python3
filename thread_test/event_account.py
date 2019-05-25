#-*- coding:utf-8-*-

import threading

class Account:
    #定义构造函数
    def __init__(self,account_no,balance):
        self.account_no = account_no
        self._balance = balance
        self.lock = threading.Lock()
        self.event = threading.Event()

    #提供只读方法
    def getBalance(self):
        return self._balance
    #提供线程安全的取钱操作
    def draw(self,draw_amount):
        #加锁
        self.lock.acquire()
        #如果event内部旗标为True，表明账户中已有人存钱进去
        if self.event.is_set():
            #执行取钱操作
            print(threading.current_thread().name+'取钱:'+str(draw_amount))
            self._balance -=draw_amount
            print('账户余额为：'+str(self._balance))
            #将event内部旗标设为False
            self.event.clear()
            #释放加锁
            self.lock.release()
            #阻塞当前线程
            self.event.wait()
        else:
            #释放加锁
            self.lock.release()
            self.event.wait()

    def deposit(self,deposit_amount):
        #加锁
        self.lock.acquire()
        if not self.event.is_set():
            #存钱
            print(threading.current_thread().name+'存钱：'+str(deposit_amount))
            self._balance +=deposit_amount
            print('账户余额为：'+str(self._balance))
            #设置event内部旗标为True
            self.event.set()
            #释放加锁
            self.lock.release()
            #阻塞当前线程
            self.event.wait()
        else:
            #释放加锁
            self.lock.release()
            #阻塞当前线程
            self.event.wait()