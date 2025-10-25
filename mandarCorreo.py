import smtplib

from config import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

your_email = api_myemail
your_password = api_key

recipent = 'jesuscadena27@hotmail.com'

message =MIMEMultipart()
message['From'] = your_email
message['To'] = recipent
message['Subject'] = 'Email de agradecimiento'

body = 'Muchas gracias a todos por el apoyo! Seguimos siendo más y trabajemos como equipo.'
message.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(your_email, your_password)

smtp_server.sendmail(your_email, recipent, message.as_string())

smtp_server.quit()

print('Email enviado correctamente.')
