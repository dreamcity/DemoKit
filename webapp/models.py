from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db


DB_NAME = 'demoKit_db'
USERS_COLLECTION = 'users'
UID_COLLECTION = 'uid'


		
class User(UserMixin):
	"""docstring for User"""
	def __init__(self,username,email,password):
		super(User, self).__init__()
		self.username = username
		self.email = email
		self.password_hash = generate_password_hash(password)

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)		
