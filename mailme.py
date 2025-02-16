""" Python SMTP program (gmail) """

import smtplib

__version__ = "1"
__author__ = "@rasta0981 - Darren K."


# -----------------------------------------------
# Simple Python email program for sending mail
# -----------------------------------------------
user_email = input("Your Email: ")
subject = input("Subject: ")
sender_email = "<Default gmail address of sender>" # replace with sender email
mail_message = input("Message: ")
text = f"Subject: {subject}\n\n{mail_message}"
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, "<gmail app code>") # requires gmail app code
server.sendmail(sender_email, user_email, text)
# -----------------------------------------------
