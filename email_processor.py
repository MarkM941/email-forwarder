import email, imaplib, smtplib, os

amazon_email = os.getenv("amazon_email")
amazon_password = os.getenv("amazon_password")

name1 = os.getenv("name1")
email1 = os.getenv("email1")

name2 = os.getenv("name2")
email2 = os.getenv("email2")

name3 = os.getenv("name3")
email3 = os.getenv("email3")

def forward_emails():
    print "Forwarding emails..."

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(amazon_email, amazon_password)
    mail.select("INBOX")

    resp, items = mail.search(None, "(UNSEEN)")
    items = items[0].split()

    for email_id in items:
        resp, data = mail.fetch(email_id, "(RFC822)")
        email_body = data[0][1]
        to_addr = ""
        if name1 in email_body:
            to_addr = email1
        elif name2 in email_body:
            to_addr = email2
        elif name3 in email_body:
            to_addr = email3
        if to_addr is not "":
            print "Sending to..." + to_addr
            message = email.message_from_string(email_body)
            from_addr = "Millstein Amazon <" + amazon_email + ">"
            
            for key in message.keys():
                message.__delitem__(key)

            message.add_header("From", from_addr)
            message.add_header("To", to_addr)
            message.add_header("Content-Type", "multipart/alternative")
            message.add_header("Subject", "Amazon Order")

            smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
            smtpserver.starttls()
            smtpserver.login(amazon_email, amazon_password)
            smtpserver.sendmail(amazon_email, to_addr, message.as_string())
            smtpserver.quit()
            
            print 'done!'
