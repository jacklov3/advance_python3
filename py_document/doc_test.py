#-*- coding:utf-8-*-

def square(x):
    '''
    一个用于计算平方的函数
    例如
    >>> square(2)
    4
    >>> square(3)
    9
    >>> square(-3)
    9
    '''
    return x**2
if __name__=='__main__':
    import doctest
    doctest.testmod()