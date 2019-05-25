#-*- coding:utf-8-*-

import  sqlite3

#定义一个普通函数，准备注册为SQL中自定义函数

def reverse_ext(st):
    return '['+st[::-1]+']'

#连接数据库
conn = sqlite3.connect('first.db')
#注册自定义函数:enc
conn.create_function('enc',1,reverse_ext)
#获取游标
c =conn.cursor()
#在sql中使用该enc自定义函数
c.execute('insert into user_tb values (null,?,enc(?),?)',('贾宝玉','123456','male'))
conn.commit()

#关闭游标
c.close()
#关闭连接
conn.close()
