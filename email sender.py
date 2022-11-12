from email.message import EmailMessage
import subprocess
import ssl
import smtplib

email_sender = 'thaenalpha@gmail.com'
email_password = subprocess.run(["pass", "Email/thaenalpha@gmail.com/python"],
                                capture_output=True, text=True).stdout
email_receiver = 'ninemsn_catarrhal@simplelogin.com'

subject = "Dont forget to subscribe"
body = """
When you watch a video, please hit subscribe
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
