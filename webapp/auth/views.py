from flask import render_template
from . import auth


@auth.route('/sign_in')
def sign_in():
    return render_template('auth/sign_in.html')

@auth.route('/sign_up')
def sign_up():
    return render_template('auth/sign_up.html')

