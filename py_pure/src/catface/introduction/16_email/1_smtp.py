from email.mime.text import MIMEText

msg = MIMEText('hi, catface', 'plain', 'utf-8')  # 构造邮件

from_addr = 'catface.wyh@foxmail.com'
password = 'qqqaaa'

to_addr = 'catface.wyh@foxmail.com'
smtp_server = 'smtp.qq.com'  # SMTP服务器地址

import smtplib

server = smtplib.SMTP(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password=password)
server.sendmail(from_addr=from_addr, to_addrs=[to_addr], msg=msg.as_string())
server.quit()
