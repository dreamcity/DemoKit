from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

from .. import db
from ..models import *

class LoginForm(FlaskForm):
	email = StringField('Email Address', validators=[Required(), Length(1, 64),Email()])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('Keep me logged in')
	submit = SubmitField('Signin')

class SignupForm(FlaskForm):
	username = StringField('Username', validators=[
						Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
						'Usernames must have only letters, ''numbers, dots or underscores')])
	email = StringField('Email Address', validators=[Required(), Length(1, 64),Email()])
	password = PasswordField('Password', validators=[
	Required(), EqualTo('password2', message='Passwords must match.')])
	password2 = PasswordField('Confirm Password', validators=[Required()])
	submit = SubmitField('Signup')
	def validate_email(self, field):
		if db[DB_NAME][USERS_COLLECTION].find_one({"email":field.data}):
			raise ValidationError('Email already registered.')

	def validate_username(self, field):
		if db[DB_NAME][USERS_COLLECTION].find_one({"username":field.data}):
			raise ValidationError('Username already in use.')


class PasswordForm(FlaskForm):
	old_pwd = PasswordField('Old Password', validators=[Required()])
	new_pwd = PasswordField('New Password', validators=[Required()])
	confirm_pwd = PasswordField('Confirm Password', validators=[Required(),EqualTo('new_pwd', message='Passwords must match.')])
	submit = SubmitField('Update Password')
