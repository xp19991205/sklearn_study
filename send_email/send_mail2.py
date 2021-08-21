# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# smtp_obj = smtplib.SMTP_SSL("smtp.exmail.qq.com",465)
# smtp_obj.login("1197386970@qq.com","xfotqgakbqlwhjcf")
# msg = MIMEText("测试数据，只做测试用途")
# msg["From"] = Header("来自徐棚的问候",'utf-8')
# msg['To'] = Header("接受徐棚的问候",'utf-8')
# msg["Subject"] = Header("这是主题",'utf-8')
# smtp_obj.sendmail("1197386970@qq.com",["1197386970@qq.com"],msg.as_string())

# !/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '1197386970@qq.com'
receivers = ['1197386970@qq.com','202112021063t@cqu.edu.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
mail_message = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""
message = MIMEText(mail_message,'html','utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')  # 发送者
message['To'] = Header("测试", 'utf-8')  # 接收者

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
smtpObj.login('1197386970@qq.com','xfotqgakbqlwhjcf')
try:
    # smtpObj.login('1197386970@qq.com','xfotqgakbqlwhjcf')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("success")
    print
    "邮件发送成功"
except smtplib.SMTPException:
    print("fail")
    print
    "Error: 无法发送邮件"
