#-*- coding:utf-8 -*-

import  sqlite3

#连接数据库
conn = sqlite3.connect('first.db')

#获取游标
c = conn.cursor()

#执行查询语句,查询id大于2的记录
c.execute('select * from user_tb where _id>?',(2,))

print('查询返回的记录数:',c.rowcount)
for col in (c.description):
    print(col[0],end='\t')
print('\n----------------')
while True:
    #获取一行记录，每行数据都是一个元组
    # row = c.fetchone()
    # #如果抓取的row为None,退出循环
    # if not row:
    #     break
    # print(row)
    # print(row[1]+'-->'+row[2])

    #也可一次获取多条记录
    rows = c.fetchmany(3)
    if not rows:
        break
    for r in rows:
        print(r)

    #fetchall不知道记录有多少，可能会让导致内存开销过大，系统崩溃，应该慎用或不用

#关闭游标
c.close()
#关闭连接
conn.close()


