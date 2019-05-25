# -*- coding:utf-8 -*-

import sqlite3

# connect

conn = sqlite3.connect('first.db')

# get cursor
c = conn.cursor()

# insert

# c.execute('insert into user_tb values(null,?,?,?)',('孙悟空','123456','male'))
#
# c.execute('insert into order_tb values(null,?,?,?,?)',('鼠标','34.2','3','1'))

# # insert many by once
# c.executemany('insert into user_tb values(null,?,?,?)', (
#     ('sun', '123456', 'male'),
#     ('bai', '123456', 'female'),
#     ('zhu', '123456', 'male'),
#     ('niu', '123456', 'male'),
#     ('tang', '123456', 'male')
# ))

#update all by once

c.executemany('update user_tb set name=? where _id=?',(
    ('小孙',2),
    ('小白',3),
    ('小猪',4),
    ('小牛',5),
    ('小唐',6)

))

#获取被修改的记录条数
print('修改的记录条数:',c.rowcount)
# 提交事务
conn.commit()

# 关闭游标和连接
c.close()
conn.close()
