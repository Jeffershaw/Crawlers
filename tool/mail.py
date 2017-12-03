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


def EMailFunc():
    sttr=""
    flag1=False
    TInfo=Catch.Catch("Manchester United")
    for i in TInfo:
        sttr=sttr+i+":"+TInfo[i]+"\n"
        print i+TInfo[i];
        if(TInfo[i]=='Buy Now'):
            flag1=True
    if flag1:
        return True,sttr
    else:
        return False,sttr


if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S', filename='myapp.log', filemode='w')
    logging.info("Program start")
    flag = False
    flag1 = False
    timecounter=12*60*60
    sttr=""
    i=0
    while(True):
        flag1,sttr = EMailFunc()
        if flag1 and not flag:
            if send_mail(mailto_list, "门票信息", sttr):
                logging.info("可以抢票 发送成功")
            else:
                logging.info("可以抢票 发送失败")
            flag = True
        if timecounter==0:
            if send_mail(mailto_list, "门票信息", sttr):
                logging.info("暂时不可以抢票 发送成功 重置时间")
            else:
                logging.info("暂时不可以抢票 发送失败 重置时间")
            timecounter=60*60*24
        sleep(600)
        timecounter-=600
        i=i+1
        logging.info(str(i)+"循环-10m")