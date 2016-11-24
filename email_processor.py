import email, imaplib, smtplib, os


def forward_emails():
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
        if to_addr is not "":
            print "Sending to..." + to_addr
            message = email.message_from_string(email_body)
            
            from_addr = "Millstein Amazon <" + amazon_email + ">"
            message.replace_header("To", "m.millstein1234@gmail.com")
            message.replace_header("From", from_addr)

            smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
            smtpserver.starttls()
            smtpserver.login(amazon_email, amazon_password)
            smtpserver.sendmail(amazon_email, to_addr, message.as_string())
            smtpserver.quit()
            
            print 'done!'


def test_emails():
    imap_host = "imap.gmail.com"
    smtp_host = "smtp.gmail.com"
    smtp_port = 587
    user = "millstein.amazon@gmail.com"
    passwd = "Pasta123"
    from_addr = "Millstein Amazon <millstein.amazon@gmail.com>"
    to_addr = "m.millstein1234@gmail.com"

    # open IMAP connection and fetch message with id msgid
    # store message data in email_data
    client = imaplib.IMAP4_SSL(imap_host)
    client.login(user, passwd)
    client.select('INBOX')
    resp, items = client.search(None, "ALL")
    items = items[0].split()
    status, data = client.fetch(items[0], "(RFC822)")
    email_data = data[0][1]
    client.close()
    client.logout()

    # create a Message instance from the email data
    message = email.message_from_string(email_data)

    # replace headers (could do other processing here)
    message.replace_header("From", from_addr)
    message.replace_header("To", to_addr)

    # open authenticated SMTP connection and send message with
    # specified envelope from and to addresses
    smtp = smtplib.SMTP(smtp_host, smtp_port)
    smtp.starttls()
    smtp.login(user, passwd)
    smtp.sendmail(from_addr, to_addr, message.as_string())
    smtp.quit()

