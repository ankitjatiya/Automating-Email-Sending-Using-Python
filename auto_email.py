import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
mail_content = '''Respected Sir,

I have attached this week's progress report.
Please find the attachment.

Thank You

Regards,
Ankit Kumar Jatiya
'''
# Date and time script
 
today=datetime.datetime.today()
if today.weekday()==4:   #firday=4

	#The mail addresses and password
	sender_address = 'akj0147@gmail.com'
	sender_pass = 'djankit0147'
	receiver_address = 'ankit_1998@iitg.ac.in'
	#Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	message['Subject'] = "Progress Report"
	#The subject line
	#The body and the attachments for the mail
	message.attach(MIMEText(mail_content, 'plain'))
	attach_file_name = 'MTP-problem-statement.pdf'
	attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
	payload = MIMEBase('application', 'octate-stream')
	payload.set_payload((attach_file).read())
	encoders.encode_base64(payload) #encode the attachment
	#add payload header with filename
	payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
	message.attach(payload)
	#Create SMTP session for sending the mail
	session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
	session.starttls() #enable security
	session.login(sender_address, sender_pass) #login with mail_id and password
	text = message.as_string()
	session.sendmail(sender_address, receiver_address, text)
	session.quit()
	print('Mail Sent')
else:
	print('Not sent')