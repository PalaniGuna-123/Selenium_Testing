# password="jmpr djlv frsv mglh"
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
my_email ='gunahitler779@gmail.com'
password="jmpr djlv frsv mglh"
s=smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login(my_email,password)
msg=MIMEMultipart()
msg['From']=my_email
msg['To']=input('enter your email address : ')
msg['Subject']=input('enter the subject for email : ')
message=input('Enter the test message:  ')
msg.attach(MIMEText(message,'plain'))
s.send_message(msg)
print('the message sent! ')