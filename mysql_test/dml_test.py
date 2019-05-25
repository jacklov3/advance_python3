#-*- coding:utf-8-*-

import pymysql

#连接
conn = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root',password='password',database='python')

#获取游标

c = conn.cursor()

#执行dml语句
c.execute('insert into user_tb values(null,%s,%s,%s)',('孙悟空','123456','male'))

#c.execute('insert into order_tb values(null,%s,%s,%s,%s)',('鼠标','34.2','3',1))

conn.commit()
c.close()
conn.close()


