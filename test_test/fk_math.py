#-*- coding:utf-8-*-

def one_equation(a,b):
    '''
    求一元一次方程a*x+b=0的解
    参数a-方程中变量的系数
    参数b，方程中的常量
    返回方程的解
    :param a:
    :param b:
    :return:
    '''
    if a==0:
        raise ValueError('参数错误')
    #返回方程的解
    else:

        return -b/a


def two_equation(a,b,c):
     '''
     求一元二次方程a*x*x+b*x+c=0的解
     :param a: 二次幂的系数
     :param b: 变量的系数
     :param c: 方程中的常量
     :return: 方程的根
     '''
     if a==0:
         raise ValueError('参数错误')
     elif b*b - 4*a*c <0:
         raise ValueError('方程在有理数范围内无解')
     #方程有唯一的解
     elif b*b - 4*a*c == 0:
         return -b /(2*a)
     else:
         r1 = (-b+(b*b -4*a*c)**0.5)/2/a
         r2 = (-b+(b*b-4*a*c)**0.5)/2/a
         return r1,r2