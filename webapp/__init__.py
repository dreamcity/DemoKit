from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_login import LoginManager

from pymongo import MongoClient
from celery import Celery

from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class


from config import *

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()

db = MongoClient()
celery  = Celery(APP_NAME, broker=CELERY_BROKER_URL)

photos = UploadSet('photos', IMAGES)


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.signin'


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)

    celery.conf.update(app.config) 

    configure_uploads(app, photos)
    patch_request_class(app)  # set maximum file size, default is 16MB

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

