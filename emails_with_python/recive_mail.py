import imaplib
m=imaplib.IMAP4_SSL('imap.gmail.com')
import getpass
email=getpass.getpass('email: ')
psw=getpass.getpass('pass: ')
m.login(email,psw)
#print(m.list()) #givelist of all mails
print(m.select('inbox'))   #give numbers of mails in inbox
typ,data=m.search(None,'SUBJECT "test py"')
print(typ)
email_id=data[0]
result, email_data=m.fetch(email_id,'(RFC822)')
print(email_data)
raw_email=email_data[0][1]
raw_email_srting=raw_email.decode('utf-8')
import email
email_message=email.message_from_string(raw_email_srting)
for part in email_message.walk():
    if part.get_content_type=='text/plain':
        body=part.get_payload(decode=True)
        print(body)