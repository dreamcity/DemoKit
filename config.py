from pymongo import MongoClient

APP_NAME = "DemoKit"

WTF_CSRF_ENABLED = True
SECRET_KEY = 'This is a flask demoKit'
DB_NAME = 'demoKit_db'

DATABASE = MongoClient()[DB_NAME]
USERS_COLLECTION = DATABASE.user

DEBUG = True
