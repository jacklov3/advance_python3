import pymysql


# 连接
conn = pymysql.connect(user='root',password='password',host='localhost',port=3306,database='python')

# 获取游标
c = conn.cursor()

# 执行DDL语句创建数据表
c.execute('''
create table user_tb(
    user_id integer primary key auto_increment,
    name varchar(255),
    pass varchar(255),
    gender varchar(255)
)''')

#再建立一个表
c.execute('''create table order_tb(
    order_id integer primary key auto_increment,
    item_name varchar(255),
    item_price double,
    item_number double,
    user_id int,
    foreign key(user_id) references user_tb(user_id)
)''')

#关闭
c.close()
conn.close()
