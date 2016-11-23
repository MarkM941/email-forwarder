import email, imaplib, smtplib, os


def forward_emails():
    smtp_host = "smtp.gmail.com"
    smtp_port = 587
    amazon_email = "millstein.amazon@gmail.com" # os.getenv("amazon_email")
    amazon_password = "Pasta123" # os.getenv("amazon_password")

    print "Forwarding email..."
    print "Email..." + amazon_email
    print "Password..."+ amazon_password

    m = imaplib.IMAP4_SSL("imap.gmail.com")
    m.login(amazon_email, amazon_password)
    m.select("INBOX")

    resp, items = m.search(None, "ALL")
    items = items[0].split()

    for emailid in items:
        resp, data = m.fetch(emailid, "(RFC822)")
        email_body = data[0][1]
        to_addr = ""
        if "Mark Millstein" in email_body:
            to_addr = "m.millstein1234@gmail.com" # os.getenv("mark_email")
        print "To..." + to_addr
        if to_addr is not "":
            message = email.message_from_string(email_body)
            smtpserver = smtplib.SMTP("smtp.gmail.com",587)
            smtpserver.starttls()
            smtpserver.login(amazon_email, amazon_password)
            message.replace_header("To", to_addr)
            message.replace_header("From", amazon_email)
            message.replace_header("Subject", "Amazon Order")
            smtpserver.sendmail(amazon_email, to_addr, message.as_string())
            print 'done!'
            smtpserver.close()

forward_emails()
