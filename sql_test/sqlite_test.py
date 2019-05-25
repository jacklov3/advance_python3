# -*-coding:utf-8-*-
# 导入访问SQlite的模块

import sqlite3

# 打开或者创建数据库

conn = sqlite3.connect('first.db')

# 获取游标

c = conn.cursor()

# 执行DDL语句创建数据表
c.execute('''create table user_tb(
    _id integer primary key autoincrement,
    name text,
    pass text,
    gender text)''')

# 创建另一个数据表
c.execute('''create table order_tb(
    _id integer primary key autoincrement,
    item_name text,
    item_price real,
    item_number real,
    user_id integer ,
    foreign key(user_id) references user_td(_id))''')

# 关闭游标
c.close()

# 关闭连接
conn.close()
