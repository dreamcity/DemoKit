import os

from flask import current_app, render_template

from . import celery
from . import MAIL_SENDER


@celery.task
def send_async_email(sender,subject,recipients,mail_msgfile):
    msg_code ="mailx -a 'Content-Type: text/html' -r %s -s '%s'  %s < %s" %(sender,subject," ".join(recipients),mail_msgfile)
    #print("msg_code:",msg_code)
    os.system(msg_code)
    os.system("rm %s"%(mail_msgfile))

def send_email(to,subject, template, **kwargs):
    sender = MAIL_SENDER
    recipients = to.split(" ") 
    msg_body = render_template(template + '.html', **kwargs)
    mail_msgfile = "mailmsg_tmp.html"
    file_object = open(mail_msgfile, 'w')
    file_object.write(msg_body)
    file_object.close()
    send_async_email.delay(sender,subject,recipients,mail_msgfile)




