#这是发送学生成绩单/员工工资条的程序
import pandas as pd #用于读取excel中的数据
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '1197386970@qq.com'
smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
smtpObj.login('1197386970@qq.com','xfotqgakbqlwhjcf') #先进行一次登录


#读取excel数据并获取邮箱
df = pd.read_excel('./成绩单.xlsx')
data_columns = df.columns #获取所有表头
data = df.values #获取所有数据
head = "<tr>" #读取一行数据
for a in range(len(data_columns)):
    head += f"<td>{data_columns[a]}</td>"
head += "<tr/>"
for k in range(df.shape[0]):
    row_text = head
    row_text += "<tr>" #读取一行数据
    receiver_mail = data[k][0]
    for m in range(df.shape[1]):
            row_text += f"<td>{data[k][m]}</td>"
            # html_data += text
    row_text += "</tr>"
    print(row_text)
    # stu_mum = data[k][0]
    # receiver_mail = data[k][1]
    name = data[k][2]
    # score1 = data[k][3]
    # score2 = data[k][4]
    # score3 = data[k][5]
    # # print(name,receiver_mail,score1,score2,score3)
    # user_data = str(stu_mum) + name +str(score1) +str(score2) +str(score3)
    mail_body_context = f'''
    <h3> 你好.{name} <h3>
    <p>请查看你本月的成绩单<p>
    <table border="1px solid black">
    {row_text}
    </table>
    '''
    msg_body = MIMEText(mail_body_context,'html','utf-8')
    msg_body['From'] = Header("XX学校教务处", 'utf-8')  # 发送者
    msg_body['To'] = Header("202102学期成绩单", 'utf-8')  # 接收者

    subject = '成绩单'
    msg_body['Subject'] = Header(subject, 'utf-8')
    # print(receiver_mail)
    smtpObj.sendmail(sender, receiver_mail, msg_body.as_string())
    # print(k)
