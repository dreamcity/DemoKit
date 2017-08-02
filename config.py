
APP_NAME = "DemoKit"

WTF_CSRF_ENABLED = True
SECRET_KEY = 'This is a flask demoKit'

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

FLASKY_MAIL_SUBJECT_PREFIX = "helloworld"
MAIL_SERVER = '192.168.0.118'
MAIL_PORT = 25
MAIL_USE_TLS = True

FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
FLASKY_MAIL_SENDER = 'DemoKit'
FLASKY_ADMIN = 'FLASKY_ADMIN'


DEBUG = True
