#send email to others and sending file is also available
#writer:bjyhappy
#email:513431626@qq.com

#coding=gbk

import smtplib
import os
import sys
import mimetypes
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

msg = MIMEMultipart()

path = r'C:\Users\Bjy_PC\Desktop\Sendemail'
if not os.path.exists(path):
    print path,' 目录不存在!'
    
else:
   
    file1 = os.listdir(path)

    ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    for each in file1:
    
        fb1 = open(os.path.join(path,each),'rb')
        doc = MIMEBase(maintype, subtype)
        doc.set_payload(fb1.read())
        encoders.encode_base64(doc)
        doc.add_header('Content-Disposition', 'attachment; filename=%s'%each)
        fb1.close()
        msg.attach(doc)
    
   
    s=smtplib.SMTP('smtp.qq.com')
    user = 'XXXX@XX.com'
    print '账号为：XXXX@XX.com'
    msg['From']=user
    msg['To']=user

    pass_=raw_input('请输入密码：')
    s.login(user, pass_)

    if s.ehlo('hello'):
        print '登陆成功！'
    choice = raw_input('是否传递文件？("y"表示传送，其他键表示不传送)：')
    if choice == 'y':
        s.sendmail(user,user,msg.as_string())
        print '文件传递成功，再见！'
        s.quit()
    else:
        print '再见！'
raw_input()
    
    