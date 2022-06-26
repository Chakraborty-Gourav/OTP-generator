import smtplib
import random

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from_ = 'cgourav472@gmail.com'
your_pass = "waxrfyjsyxoupokx"
generated=''
name=''
id=''
def generate():
    otp=str(random.randrange(100000,999999)) 
    return otp

def establisconn(  name, to, otp):
    body = str("HELLO "+name+" YOUR OTP IS :"+otp+". IF YOU DIDN'T ASK FOR THIS, PLEASE IGNORE.")
    subject = 'OTP GENERATOR'
    message = MIMEMultipart()
    message['From'] = from_
    message['To'] = to
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    text = message.as_string()
    return text
#details={}

def send(text, to):
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(from_,your_pass)
    mail.sendmail(from_,to, text)
    mail.close()
    #print('Mail had been sent succesfully')