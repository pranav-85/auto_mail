from auto_mail import BulkMailer

mailer = BulkMailer(
    username="cs22b1027@iiitdm.ac.in",
    password="tjjj tlrm denu ayzm",
    file_path="test/test.csv",
    smtp_server="smtp.gmail.com",
    smtp_port=587
)

mailer.bulk_mail_with_message(
    mail_to_column="Email",
    subject_column="Subject",
    body_column="Message"
)