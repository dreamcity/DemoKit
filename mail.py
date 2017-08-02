#!/usr/bin/env python
import os
from flask import Flask
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.route('/', methods=['GET', 'POST'])
def index():
    to = "1296587125@qq.com"
    subject = "helloworld"
    template = "webapp/templates/auth/email/confirm.html"
    token = b'eyJhbGciOiJIUzI1NiIsImV4cCI6MTUwMTY3MDcxOSwiaWF0IjoxNTAxNjY3MTE5fQ.eyJjb25maXJtIjoxMn0.UTW4OFd5cLW_ocn_oqvkt0wngxwwiEG891bltU3VXKc'
    send_email(to,subject,template)

    return "helloworld"
    #return redirect(url_for('index'))

def send_email(to, subject, template, **kwargs):
    print("semd mail: ",to,subject,template)
    recipients = to.split(" ") 
    #msg_body = render_template(template + '.html', **kwargs)
    msg_body = template
    print("msg_body: ",msg_body)
     
    send_async_email.delay(subject,recipients,msg_body)
    #send_async_email(subject,recipients,msg_body)

    print("msg_body: ",msg_body)

@celery.task
def send_async_email(subject,recipients,msg_body):
    msg_code ="mail -s '%s' %s < %s" %(subject," ".join(recipients),msg_body)
    print("msg_code: ",msg_code)
    os.system(msg_code)

if __name__ == '__main__':
    app.run()
