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
        server.ehlo_or_helo_if_needed()
        server.starttls(context=context)
        server.ehlo_or_helo_if_needed()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)