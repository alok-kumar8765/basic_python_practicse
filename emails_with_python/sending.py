import smtplib
smtp_obj=smtplib.SMTP('smtp.gmail.com',587) #587 is port number
smtp_obj.ehlo()
smtp_obj.starttls()
#use this if your port is 587, ths is for TSL setup
import getpass
#this will help to hide your password when you type
password=getpass.getpass('Enter paasword: ')
email=getpass.getpass('enter email id: ')
smtp_obj.login(email,password)
from_add=getpass.getpass('email')
to_add=getpass.getpass('email')
subj=input('enter subject line:')
message=input('enter message: ')
msg='Subject: '+ subj + '\n' +message
smtp_obj.sendmail(from_add,to_add,msg)
smtp_obj.quit()