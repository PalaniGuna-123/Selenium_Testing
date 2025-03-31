import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

my_email = 'gunahitler779@gmail.com'
password = 'jmpr djlv frsv mglh'  
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login(my_email, password)

msg = MIMEMultipart()
msg['From'] = my_email
msg['To'] = input('Enter the recipient email address: ')
msg['Subject'] = input('Enter the subject for the email: ')
message = input('Enter your message: ')
msg.attach(MIMEText(message, 'plain'))

file_path = r"C:\Selenium_Testing\Email_Automation\Resume.png"
try:
    with open(file_path, 'rb') as file:
        part = MIMEApplication(file.read(), Name='Resume.png')
        part['Content-Disposition'] = 'attachment; filename="Resume.png"'
        msg.attach(part)
        print("Image attached successfully.")
except FileNotFoundError:
    print("Error: Image not found. Please check the path.")


s.send_message(msg)
print('Email sent successfully!')


s.quit()
