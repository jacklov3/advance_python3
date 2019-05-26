#-*- coding:utf-8-*-
'''
    简单的邮件发送，需要开头smtp
'''
import smtplib
from email.message import EmailMessage
#定义smtp服务器地址:
smtp_server = 'smtp.163.com'
#定义发件人地址
from_addr = 'xxxxx@163.com'
#定义登陆邮箱的密码
password ='***********'

#定义收件人地址:
to_addr = 'xxxxxxxx@qq.com'

#创建SMTP连接
conn = smtplib.SMTP_SSL(smtp_server,465)
conn.set_debuglevel(1)
conn.login(from_addr,password)
#创建邮件对象
msg = EmailMessage()
msg.set_content('您好，这是一封来自python的邮件','plain','utf-8')
msg['subject'] = '一封HTML邮件'
msg['from']='风中一匹狼<%s>'%from_addr
msg['to']='新用户<%s>'%to_addr
#发送邮件
conn.sendmail(from_addr,to_addr,msg.as_string())
#退出连接
conn.quit()
