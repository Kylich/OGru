def sending(EText, JT):
    # import necessary packages
    
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib
    # create message object instance
    msg = MIMEMultipart()
    
    message = '%s' % '\n '.join(JT)
    
    # setup the parameters of the message
    password = "Gorod4Narodov"
    msg['From'] = "opengamerroller@gmail.com"
    msg['To'] = "opengamerreport@gmail.com"
    msg['Subject'] = EText
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    #create server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()