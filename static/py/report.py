def sending(EText, JT):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib


    msg = MIMEMultipart()
    
    message = '%s' % '\n '.join(JT)
    
    password = 'Gorod4Narodov'
    msg['From'] = "opengamerroller@gmail.com"
    msg['To'] = "opengamerreport@gmail.com"
    msg['Subject'] = EText
    
    msg.attach(MIMEText(message, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login(msg['From'], password)

    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()