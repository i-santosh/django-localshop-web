import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


def generateVerificationCode(userEmail):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        senderEmail = '__email__'
        #my_secret = os.environ['email']
        email_password = '__passwd__'
        connection.login(senderEmail, email_password )
        msgs = MIMEMultipart('alternative')
        msgs['Subject'] = "Your 5-Digit Verification Code for LocalShop"
        msgs['From'] = senderEmail
        msgs['To'] = userEmail
        otp = random.randint(10000,99999)
        text = (f"Your Verification code is : {otp}.\n Thank you for Registering LocalShop")
        html = (f"""\
        <html>
          <head></head>
          <body>
            <h3 style='text-align:center;'>Your <b>OTP</b> for LocalShop is :<br> <button style="outline:none;margin-top:1em;border-radius:0.2em;border-width:0;text-align:center; font-size:30px;height:2em;" > <b>{otp}</b></button></h3>.<br>You OTP is valid for 10 Minutes.<br>
            <p>Thank you for Registering LocalShop.
            </p>
          </body>
        </html>
        """)
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        msgs.attach(part1)
        msgs.attach(part2)
        connection.sendmail(from_addr=senderEmail, to_addrs=userEmail,
        msg=msgs.as_string())
        return otp

