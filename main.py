'''
    1.加载所有的测试用例
    2.执行用例并生成测试报告
'''
from HTMLTestRunner import HTMLTestRunner
import unittest


# 1.加载所有用例
tests = unittest.defaultTestLoader.discover(r"D:\项目\day13【单元测试】\代码\day13",pattern="Test*.py")

# 2.创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = "计算器的测试报告",
    description="这是加法测试报告",
    verbosity=1,
    stream = open(file="计算器.html",mode="w+",encoding="utf-8")
)

# 3.执行用例
runner.run(tests)




# 4.任务： 使用邮件发送附件，把报告发送给我

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_host = 'smtp.163.com'

mail_user = 'lxbluciano'

mail_pass = 'SCAXBMZKMATROECK'

sender = 'lxbluciano@163.com'

receivers = ['454852796@qq.com']

subject = "附件"
message = MIMEMultipart()
message['Subject'] = Header(subject,'utf-8')
message['From'] = Header(sender,'utf-8')
message['To'] = receivers[0]

message.attach(MIMEText('这是lxb的计算机', 'plain', 'utf-8'))

att = MIMEText(open("D:\项目\day13【单元测试】\代码\day13\计算器.html", "rb").read(), "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = "attachment;filename = '计算器.html'"
message.attach(att)



try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(
        sender,receivers,message.as_string())
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('error',e)


