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
    print path,' Ŀ¼������!'
    
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
    print '�˺�Ϊ��XXXX@XX.com'
    msg['From']=user
    msg['To']=user

    pass_=raw_input('���������룺')
    s.login(user, pass_)

    if s.ehlo('hello'):
        print '��½�ɹ���'
    choice = raw_input('�Ƿ񴫵��ļ���("y"��ʾ���ͣ���������ʾ������)��')
    if choice == 'y':
        s.sendmail(user,user,msg.as_string())
        print '�ļ����ݳɹ����ټ���'
        s.quit()
    else:
        print '�ټ���'
raw_input()
    
    