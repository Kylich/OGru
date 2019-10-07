def sending(EText, JT):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib
    import os
    import sys
    from boto.s3.connection import S3Connection

    msg = MIMEMultipart()
    message = '%s' % '\n '.join(JT)
    
    try:
        password = S3Connection('S3_pass')
    except:
        print('1 pass fail')
        print(sys.exc_info())
        try:
            password = str(S3Connection(os.environ['S3_pass']))
        except:
            print('2 pass fail')
            print(sys.exc_info())
            return

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
