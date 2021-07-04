import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class email:
    def simple(to,sub,body):
         user = ********
         server = smtplib.SMTP('smtp.gmail.com', 587)
         msg = MIMEMultipart('alternative')
         msg['Subject'] = sub
         me = user
         family = [to]
         msg['From'] = me
         msg['To'] = ', '.join(family)
         body = body
         msg.attach(MIMEText(body,'plain','utf-8'))
         server.starttls()
         server.login(user,********)
         server.sendmail(me,family, msg.as_string())
         server.quit()
      
    def html(to, sub, code):
        me = ********
        you = to
        msg = MIMEMultipart('alternative')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = you
        text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
        html = f"""\
        <html>
          <head></head>
          <body>
           {code}
          </body>
        </html>
        """
        part2 = MIMEText(html, 'html')
        
        
        msg.attach(part2)
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(me,********)
        server.sendmail(me, you, msg.as_string())
        server.quit()
