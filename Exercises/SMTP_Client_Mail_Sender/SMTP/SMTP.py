import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = input("Type your Email Address and press enter: ")
password = input("Type your Email Password and press enter: ")
receiver_email = input("Type your Receiver Email Address and press enter: ")


message = MIMEMultipart("alternative")
message["Subject"] = input("Type your Email Subject and press enter: ")
message["From"] = sender_email
message["To"] = receiver_email

tmp_msg = input("Type your Email Message Content and press enter: ")

# Create the plain-text and HTML version of your message
text = """\
%s
""" %(tmp_msg)


# Turn these into plain MIMEText objects
part1 = MIMEText(text, "plain")


# Add plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)


# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.close()
    print("Email sent.")
