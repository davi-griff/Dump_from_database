import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from environs import Env

class Email():
    def __init__(self):
        pass

    env = Env()

    env.read_env()

    def inst_smtp(self,subject,tetx='Conteúdo do Email',attachments=[]):
        
        msg = MIMEMultipart()
        msg['From'] = env("SMTP_MAIL")
        msg['To'] = 'siac.deacbd@gmail.com'
        msg['subject'] = subject
        msg.attach(MIMEText(text))

        for attach in attachments:
            attach = open(attach, 'rb')

        return msg

    