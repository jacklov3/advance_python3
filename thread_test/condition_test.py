#-*- coding:utf-8-*-

import threading

class Account:
    #定义构造器
    def __init__(self,account_no,balance):
        self.account_no = account_no
        self._balance = balance
        self.cond = threading.Condition()
        #定义代表是否已经存钱的旗标
        self._flag = False

    def getBalance(self):
        return self._balance

    #线程安全的draw()方法来完成取钱操作
    def draw(self,draw_amount):
        #加锁，相当于调用Condition绑定的Lock的acquire()
        self.cond.acquire()
        try:
            #如果self._flag为假，表明账户中还没有人存钱进去，取钱方法阻塞
            if not self._flag:
                self.cond.wait()
            else:
                #执行取钱操作
                print(threading.current_thread().name+'取钱：'+str(draw_amount))
                self._balance -=draw_amount
                print("账户余额为："+str(self._balance))
                #将标识账户是否已有存款的旗标设置为False
                self._flag = False
                #唤醒其它线程
                self.cond.notify_all()
        finally:
            self.cond.release()

    def deposit(self,deposit_amount):
        #加锁
        self.cond.acquire()
        try:
            #为真，则表示有钱，存钱方法阻塞
            if self._flag:
                self.cond.wait()
            else:
                #执行存款操作
                print(threading.current_thread().name+'存款:'+str(deposit_amount))
                self._balance +=deposit_amount
                print("账户余额为:"+str(self._balance))
                #改变flag
                self._flag = True
                #唤醒其他线程
                self.cond.notify_all()
        finally:
            self.cond.release()

#定义一个函数，模拟重复max次执行取钱操作
def draw_many(account,draw_amount,max):
    for i in range(max):
        account.draw(draw_amount)

#定义一个函数，模拟重复max次执行存款操作
def deposit_many(account,deposit_amount,max):
    for i in range(max):
        account.deposit(deposit_amount)

#创建一个用户
acct = Account('1234567',0)
#创建、并启动一个'取钱'线程
threading.Thread(name='取钱者',target=draw_many,args=(acct,800,100)).start()
#创建、并启动一个'存款'线程
threading.Thread(name='存款者甲',target=deposit_many,args=(acct,800,100)).start()
threading.Thread(name='存款者乙',target=deposit_many,args=(acct,800,100)).start()
threading.Thread(name='存款者丙',target=deposit_many,args=(acct,800,100)).start()

