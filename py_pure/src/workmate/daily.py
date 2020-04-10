#!/usr/bin/python
# -*- coding: UTF-8 -*-


import smtplib
import urllib
import urllib.request
# import urllib2
import time

from email.mime.text import MIMEText
from email.header import Header

PATH = ""

daily_people_list = []
mail_recive_list = []


def read_conf():
    with open("./mail.conf", "rb") as addresses:
        for address in addresses:
            mail_recive_list.append(address)
    with open("./daily.ini", "rb") as peoples:
        for people in peoples:
            daily_people_list.append(people)


def send_mail(peoples):
    smtpObj = smtplib.SMTP()
    smtpObj.connect("", 25)
    smtpObj.login("", "")
    now = time.strftime("%Y%m%d", time.localtime())

    html = """
                <table color="CCCC33" width="800" border="1" cellspacing="0" cellpadding="5" text-align="center" height="50">
                        <tr>
                                <td text-align="center">姓名</td>
                                <td text-align="center">填写情况</td>
                                <td height="150">当天工作情况</td>
                                <td height="150">次日工作计划</td>
                                <td height="150">问题&amp;解决进展</td>
                        </tr>                        
            """
    for people in peoples:
        one_peole = """<tr>   
                                <td text-align="center">%s </td>
                                <td>%s </td>
                                <td>%s </td>
                                <td>%s </td>
                                <td>%s </td>
                       </tr>
                    """ % (people.get("name"), \
                           people.get("write"), \
                           people.get("today", ""), \
                           people.get("nextday", ""), \
                           people.get("problem", ""))
        html = html + one_peole
    html = html + "</table>"

    message = MIMEText(html, 'html', 'utf-8')
    message['From'] = Header("nfv_devops@asiainfo.com", 'utf-8')

    recive = ""
    for index, mail_recive in enumerate(mail_recive_list):
        recive = recive + mail_recive.strip()
        if index != len(mail_recive_list) - 1:
            recive = recive + ','
    message['To'] = Header(recive, 'utf-8')
    message['Subject'] = "项目每日日报汇总-" + now
    smtpObj.sendmail("", mail_recive_list, message.as_string())


def read_daily():
    ret = []
    now = time.strftime("%Y%m%d", time.localtime())
    for name in daily_people_list:
        people = {}
        people["name"] = name
        str = urllib.request.quote(name.decode('UTF-8').encode('utf8'))
        try:
            # response = urllib2.urlopen(PATH + str + ":" + now)
            response = urllib.request.urlopen(PATH + str + ":" + now)
            for line in response.read().split("\n"):
                people["write"] = "已填写"
                if "当天工作情况" in line:
                    people["today"] = line.split(">")[3][:-4]
                if "次日工作计划" in line:
                    people["nextday"] = line.split(">")[3][:-4]
                if "解决进展" in line:
                    people["problem"] = line.split(">")[3][:-4]
        except:
            people["write"] = "未填写"
        if people.get("today", "").strip() == "":
            people["write"] = "未填写"
        ret.append(people)
    return ret


if __name__ == '__main__':
    read_conf()
    daily = read_daily()
    send_mail(daily)
