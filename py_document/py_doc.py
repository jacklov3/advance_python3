#-*- coding:utf-8 -*-
'''
 文档测试
'''
MY_NAME='c语言中文网'

def say_hi(name):
    '''
    定义一个打招呼的函数
    返回对指定用户打招呼的字符串
    '''
    print('执行say_hi函数')
    return name+'您好！'

def print_rect(height,width):
    '''
    定义一个打印矩形的函数
    height - 代表矩形的高
    width-代表矩形的宽
    :param height:
    :param width:
    :return:
    '''
    print(('*'*width+'\n')*height)

class User:
    NATIONAL = 'China'
    '''
    定义一个代表用户的类
    该类包括name、age两个变量
    '''
    def __init__(self,name,age):
        '''
        name初始化该用户的name
        age初始化该用户的age
        :param name:
        :param age:
        '''
        self.name = name
        self.age = age
    def eat(self):
        '''
        定义用户吃东西的方法
        food-代表用户正在吃的东西
        :return:
        '''
        print('%s正在吃%s'%(self.name,food))
