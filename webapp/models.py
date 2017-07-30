from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from . import db, login_manager

DB_NAME = 'demoKit_db'
USERS_COLLECTION = 'users'
UID_COLLECTION = 'uid'

class User(UserMixin):
	"""docstring for User"""
	def __init__(self,user_info):
		super(User, self).__init__()
		self.username = user_info["username"]
		self.email = user_info["email"]
		self.user_id = user_info["_id"]
		self.confirmed = False

	def get_id(self):
		return chr(self.user_id)

	def generate_confirmation_token(self, expiration=3600):
		s = Serializer(current_app.config['SECRET_KEY'], expiration)
		return s.dumps({'confirm': self.user_id})
	
	def confirm(self, token):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
			data = s.loads(token)
		except:
			return False
		if data.get('confirm') != self.user_id:
			return False
		self.confirmed = True
		db.session.add(self)
		return True



@login_manager.user_loader
def load_user(user_id):
	user_info = db[DB_NAME][USERS_COLLECTION].find_one({"_id":ord(user_id)})
	return User(user_info)

# class User(UserMixin, db.Model):
# 	__tablename__ = 'users'
# 	id = db.Column(db.Integer, primary_key=True)
# 	email = db.Column(db.String(64), unique=True, index=True)
# 	username = db.Column(db.String(64), unique=True, index=True)
# 	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
# 	password_hash = db.Column(db.String(128))
# 	confirmed = db.Column(db.Boolean, default=False)

# 	@property
# 	def password(self):
# 		raise AttributeError('password is not a readable attribute')

# 	@password.setter
# 	def password(self, password):
# 	self.password_hash = generate_password_hash(password)

# 	def verify_password(self, password):
# 		return check_password_hash(self.password_hash, password)

# 	def generate_confirmation_token(self, expiration=3600):
# 		s = Serializer(current_app.config['SECRET_KEY'], expiration)
# 		return s.dumps({'confirm': self.id})

# 	def confirm(self, token):
# 		s = Serializer(current_app.config['SECRET_KEY'])
# 		try:
# 		data = s.loads(token)
# 		except:
# 			return False
# 		if data.get('confirm') != self.id:
# 			return False
# 		self.confirmed = True
# 		db.session.add(self)
# 		return True

# 	def __repr__(self):
# 		return '<User %r>' % self.username







# from . import login_manager
# @login_manager.user_loader
# def load_user(user_id):
# 	return User.query.get(int(user_id))

# from flask.ext.login import login_required
# @app.route('/secret')
# @login_required
# def secret():
# 	return 'Only authenticated users are allowed!'

