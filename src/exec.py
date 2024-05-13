import smtplib #for sending verification emails through python
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(email,report):
    devhire_email = 'ashadq345@gmail.com'
    devhire_email_password = 'axax rbmv bgyp dhvw'
    mail_content = MIMEMultipart("alternative")
    mail_content['Subject'] = 'DevHire Interview Report'
    mail_content['From'] = devhire_email
    mail_content['To'] = email

    text = f"{report}"
    
    part1 = MIMEText(text,'plain')
    mail_content.attach(part1)
    
    
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=ssl.create_default_context() ) as server:
        server.login(devhire_email,devhire_email_password)
        server.send_message(mail_content)