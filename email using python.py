import smtplib         #simple mail transfer protocol
## used to send mail
from email.message import EmailMessage

email = EmailMessage()

SERVER = smtplib.SMTP_SSL("smtp.gmail.com", 465)
SERVER.login("yourmail id @gmail.com", "your mail password")
SERVER.sendmail("to@gmail.com",
                "to@gmail.com",
                "hello,how are youuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu?")

SERVER.quit()


print("email sent")






