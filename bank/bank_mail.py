# include necessary package
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# set mail information
fromAddr = ''
fromPass = ''
toAddr   = ''
msg = MIMEMultipart()
msg['From']		= fromAddr
msg['To']		= toAddr
msg['Subject']	= '[匯率觸價通知]'

# set mail content / get the last line of USD.txt
file = open('USD.txt','r', encoding='UTF-8')
line = file.readlines()	
last = line[-1]
sell1Num = float(last[15:23])

# set your Hit_price
Hit_price = 
# set if lower than Hit_price then send mail
if sell1Num < Hit_price:
	msg.attach(MIMEText(line[-1]+'\n低於 '+str(Hit_price),'plain'))
	# set mail server and do operation
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(fromAddr,fromPass)
	text = msg.as_string()
	try:
		server.sendmail(fromAddr,toAddr,text)
		print('Success:send complet')
	except smtplib.SMTPException:
		print('Error:send failed')
	server.quit()
else:
	print("No lower than Hit_price")
