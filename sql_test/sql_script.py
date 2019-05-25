# -*- coding:utf-8-*-

import sqlite3

#连接数据库
conn = sqlite3.connect('first.db')

#获取游标
c = conn.cursor()

#调用executescript()方法执行一段sql脚本

c.executescript('''
    insert into user_tb values(null,'武松','3444','male')
    insert into user_tb values (null,'林冲','44444','male')
    create table item_tb(_id integer primary key autoincrement,name,price)
''')

conn.commit()

c.close()
conn.close()