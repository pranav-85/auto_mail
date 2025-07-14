from auto_mail import AutoMailer
from dotenv import load_dotenv
import os

load_dotenv()

mailer = AutoMailer(
    username=os.getenv("MAIL_ID"),
    password=os.getenv("PASSWORD"),
    smtp_server="smtp.gmail.com",
    smtp_port=587
)

mailer.send_mail(
    to_address="saipranav.dev@gmail.com",
    subject="Test Email",
    body="This is a test email sent using AutoMailer."
)