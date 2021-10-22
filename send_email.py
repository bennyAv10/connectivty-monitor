#!/usr/bin/env python3

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.
# with open(textfile) as fp:
    # Create a text/plain message
msg = EmailMessage()
msg.set_content('my message body')

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'The contents of '
msg['From'] = 'zfdf@daf.com'
msg['To'] = 'b.avramson@gmail.com'

# Send the message via our own SMTP server.
s = smtplib.SMTP()
s.send_message(msg)
s.quit()
