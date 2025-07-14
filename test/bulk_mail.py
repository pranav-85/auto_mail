from auto_mail import BulkMailer
from dotenv import load_dotenv
import os

load_dotenv()

mailer = BulkMailer(
    username=os.getenv("MAIL_ID"),
    password=os.getenv("PASSWORD"),
    csv_path="test/test.csv",
    template_path="test/template.docx",
    smtp_server="smtp.gmail.com",
    smtp_port=587
)

mailer.bulk_mail(
    mail_to_column="Email",
    subject_column="Subject",
    body_column="Message"
)