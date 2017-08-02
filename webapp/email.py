import os

# from flask import current_app, render_template

from celery import Celery


CELERY_BROKER_URL = "redis://192.168.0.118:6379/0"
CELERY_RESULT_BACKEND = 'redis://192.168.0.118:6379/0'

celery = Celery("DemoKit", broker=CELERY_BROKER_URL)

@celery.task
def send_async_email(subject,recipients,msg_body):
    msg_code ="mail -s '%s' %s < %s" %(subject," ".join(recipients),msg_body)
    print("msg_code: ",msg_code)
    os.system(msg_code)

def send_email(to, subject, template, **kwargs):
    print("semd mail: ",to,subject,template)
    recipients = to.split(" ") 
    msg_body = template
    #msg_body = render_template(template + '.html', **kwargs)
    print("msg_body: ",msg_body)
     
    send_async_email.delay(subject,recipients,msg_body)


if __name__ == '__main__':
    to = "dream_city@126.com"
    subject = "helloworld"
    template = "templates/auth/email/confirm.html"
    token = b'eyJhbGciOiJIUzI1NiIsImV4cCI6MTUwMTY3MDcxOSwiaWF0IjoxNTAxNjY3MTE5fQ.eyJjb25maXJtIjoxMn0.UTW4OFd5cLW_ocn_oqvkt0wngxwwiEG891bltU3VXKc'
    send_email(to,subject,template)


