from flask import render_template, redirect, request, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

from . import auth
from .forms import LoginForm, SignupForm, PasswordForm
from .. import db
from ..models import *

from ..email import send_email


@auth.before_app_request
def before_request():
	if current_user.is_authenticated \
			and not current_user.confirmed \
			and request.endpoint[:5] != 'auth.'\
			and request.endpoint != 'static':
		return redirect(url_for('auth.unconfirmed'))

@auth.route('/unconfirmed')
def unconfirmed():
	if current_user.is_anonymous or current_user.confirmed:
		return redirect(url_for('main.index'))
	return render_template('auth/unconfirmed.html')



@auth.route('/signin', methods=['GET', 'POST'])
def signin():
	form = LoginForm()
	if form.validate_on_submit():
		# user_info = db[DB_NAME][USERS_COLLECTION].find_one({"email":form.email.data},projection={"password":True})
		user_info = db[DB_NAME][USERS_COLLECTION].find_one({"email":form.email.data})
		if user_info and check_password_hash(user_info["password"], form.password.data) :
			login_user(User(user_info), form.remember_me.data)

			return redirect(request.args.get('next') or url_for('main.index'))
		flash('Invalid username or password.')
	return render_template('auth/signin.html', form=form)

@auth.route('/signout')
@login_required
def signout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('main.index'))


@auth.route('/setting',methods=['GET', 'POST'])
@login_required
def setting():
	form = PasswordForm()
	if form.validate_on_submit():
		user_id = current_user.user_id
		if not check_password_hash(current_user.password_hash, form.old_pwd.data):
			flash('Password is wrong.')
		else:
			db[DB_NAME][USERS_COLLECTION].update_one({"_id":user_id},{'$set':{"password":generate_password_hash(form.new_pwd.data)}})
			return redirect(request.args.get('next') or url_for('main.index'))
		return render_template('auth/setting.html', form=form)
	return render_template('auth/setting.html', form=form)


@auth.route('/signup',methods = ['GET', 'POST'])
def signup():
	form = SignupForm()
	if form.validate_on_submit():
		uid_info = db[DB_NAME][UID_COLLECTION].find_one_and_update({"_id":"users"}, {'$inc': {"currentUID": 1}})
		uid = int(uid_info["currentUID"])
		user_info = dict({})
		user_info["username"] = form.username.data
		user_info["email"] = form.email.data
		user_info["password"] = generate_password_hash(form.password.data)
		#db[DB_NAME][USERS_COLLECTION].update_one({"_id":uid},{'$set':user_info},upsert = True)
		user_info["_id"] = uid
		user_info["confirmed"] = False
		user = User(user_info)
		token = user.generate_confirmation_token()
		send_email(user.email, 'Confirm Your Account','auth/email/confirm', user=user, token=token)
		flash('A confirmation email has been sent to you by email.')
		db[DB_NAME][USERS_COLLECTION].update_one({"_id":uid},{'$set':user_info},upsert = True)
		return redirect(url_for('auth.signin'))
	return render_template('auth/signup.html', form=form)

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
	if current_user.confirmed:
		return redirect(url_for('main.index'))
	if current_user.confirm(token):
		flash('You have confirmed your account. Thanks!')
	else:
		flash('The confirmation link is invalid or has expired.')
	return redirect(url_for('main.index'))

@auth.route('/confirm')
@login_required
def resend_confirmation():
	token = current_user.generate_confirmation_token()
	send_email(current_user.email, 'Confirm Your Account','auth/email/confirm', user=current_user, token=token)
	flash('A new confirmation email has been sent to you by email.')
	return redirect(url_for('main.index'))


                            
