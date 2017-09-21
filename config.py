import os

APP_NAME = "DemoKit"

WTF_CSRF_ENABLED = True
SECRET_KEY = 'This is a flask demoKit'

MAIL_SENDER = "admin@workspace.com"

CELERY_BROKER_URL = "redis://192.168.0.141:6379/0"
CELERY_RESULT_BACKEND = 'redis://192.168.0.141:6379/0'

UPLOADED_TEXTS_DEST  = os.getcwd() + '/storages'


DEBUG = True
