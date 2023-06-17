import smtplib


to=input("Enter the recievers email")
message=input("Enter the message to send via email")

def send_email(to,message):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("senderemail.com","password")
    server.sendmail("senderemail.com",to,message)
    server.close()

send_email(to, message)