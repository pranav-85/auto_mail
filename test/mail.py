from auto_mail import AutoMailer

mailer = AutoMailer(
    username="cs22b1027@iiitdm.ac.in",
    password="tjjj tlrm denu ayzm",
    smtp_server="smtp.gmail.com",
    smtp_port=587
)

mailer.send_mail(
    to_address="saipranav.dev@gmail.com",
    subject="Test Email",
    body="This is a test email sent using AutoMailer."
)