import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()

message = 'TESTING'

password = 'C035t@2020'
msg['From'] = 'siac.deacbd@gmail.com'
msg['To'] = 'siac.deacbd@gmail.com'
msg['subject'] = 'TESTING'

msg.attach(MIMEText(message,'plain'))

server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

server.login(msg['From'],password)

server.sendmail(msg['From'],msg['To'], msg.as_string())

server.quit()

print('mail sent successfully')