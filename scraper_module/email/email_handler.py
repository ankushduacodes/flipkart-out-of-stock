import smtplib, ssl
import os

def send_email(message):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = os.getenv('email')
    receiver_email = os.getenv('reciever')
    password = os.getenv('password')

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)