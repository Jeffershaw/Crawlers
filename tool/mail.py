# -*- coding: UTF-8 -*-

import smtplib
from time import sleep,ctime
from email.mime.text import MIMEText
import logging

mailto_list = ["xxx@qq.com"]
mail_host = "smtp.163.com"  # server
mail_user = "xxx"  # 用户名
mail_pass = "xxx"  # 口令
mail_postfix = "163.com"  #

'''
def send_mail(to_list, sub, content):
    me = "sjf" + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False
'''
def send_email(email, password, result,to_list, sub='offer',From=''):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    print('successfully login')
    msg = MIMEText(result, _subtype='plain', _charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = From
    msg['To'] = ";".join(to_list)
    server.sendmail(email, to_list, msg.as_string())
    print('results sent')
    server.quit()