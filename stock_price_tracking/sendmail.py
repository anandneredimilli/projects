import ssl
import smtplib
from email.message import EmailMessage

class SendMail:
    def __init__(self,message) -> None:
        self.email_sender = "anandn9804@gmail.com"
        self.email_password = "ptoyfxljjsjylsgl"
        self.email_receiver = self.email_sender


        self.message = message

        em = EmailMessage()
        em['From'] = self.email_sender
        em['To'] = self.email_receiver
        em['Subject'] = "Test Subject"
        em.set_content(self.message)

        context = ssl.create_default_context()

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls(context=context)
            smtp.login(self.email_sender, self.email_password)
            smtp.send_message(em)