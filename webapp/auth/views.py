from flask import render_template, redirect, request, url_for, flash
from . import auth
from .forms import LoginForm, SignupForm

from ..models import *

@auth.route('/signin')
def signin():
	return render_template('auth/signin.html')

@auth.route('/signup',methods = ['GET', 'POST'])
def signup():
	form = SignupForm()
	#print("form: ",form.email.data,form.username.data,form.password.data)
	if form.validate_on_submit():
		uid_info = db[DB_NAME][UID_COLLECTION].find_one_and_update({"_id":"users"}, {'$inc': {"currentUID": 1}})
		uid = int(uid_info["currentUID"])
		user_info = dict({})
		user_info["username"] = form.username.data
		user_info["email"] = form.email.data
		user_info["password"] = form.password.data
		db[DB_NAME][USERS_COLLECTION].update_one({"_id":uid},{'$set':user_info},upsert = True)
		flash('You can now login.')
		return redirect(url_for('auth.signin'))
	return render_template('auth/signup.html', form=form)
