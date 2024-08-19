from flask_mail             import Mail, Message
from flask                  import render_template
from flask                  import request
from flask                  import jsonify
from flask                  import Flask
from email.mime.text        import MIMEText
from email.mime.multipart   import MIMEMultipart
import smtplib, ssl
import sys


app = Flask(__name__)
mail = Mail(app)


senderEmail_address = ''
senderEmail_password = ''
receiverEmail_address = ''
senderEmail_subject = ''
senderEmail_message = ''

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

def index2():
    return render_template('index2.html')

def index3():
    return render_template('index3.html')

@app.route('/signIn', methods = ['POST'])
def signIn():
    global senderEmail_address
    global senderEmail_password
    senderEmail_address = request.form["email"]
    senderEmail_password = request.form["password"]
    return render_template('index2.html')

@app.route('/sendingEmail', methods = ['POST'])
def sendingEmail():
    global receiverEmail_address
    global senderEmail_subject
    global senderEmail_message
    receiverEmail_address = request.form["email"]
    senderEmail_subject = request.form["subject"]
    senderEmail_message = request.form["message"]
    return SendEmail()

def SendEmail():
    global senderEmail_address
    global senderEmail_password
    global receiverEmail_address
    global senderEmail_subject
    global senderEmail_message
    print(senderEmail_address,senderEmail_password,receiverEmail_address,senderEmail_subject,senderEmail_message)
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = senderEmail_address
    app.config['MAIL_PASSWORD'] = senderEmail_password
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail = Mail(app)

    msg = Message(senderEmail_subject, sender = senderEmail_address, recipients = [receiverEmail_address])
    msg.body = senderEmail_message
    mail.send(msg)
    print("Email sent.")
    return render_template('index3.html')


if __name__ == '__main__':
    app.run(debug = True)