# -*- coding: utf-8 -*-
import os
import time
import hashlib
import subprocess

# from flask import render_template, session, redirect, url_for, current_app
from flask import Flask,current_app,render_template,request,redirect,url_for,session,flash
#from flask.ext.paginate import Pagination
# from flask_paginate import Pagination

#from ..email import send_email
from . import main
from .forms import UploadForm, ActionForm
from .. import texts


@main.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


@main.route('/about')
def about():
	return render_template('about.html')

@main.route('/services')
def services():
	return render_template('services.html')

@main.route('/contact')
def contact():
	return render_template('contact.html')

@main.route('/full_width')
def full_width():
	return render_template('full_width.html')

@main.route('/sidebar')
def sidebar():
	return render_template('sidebar.html')

@main.route('/faq')
def faq():
	return render_template('faq.html')

@main.route('/404')
def error_404():
	return render_template('404.html')

@main.route('/pricing')
def pricing():
	return render_template('pricing.html')
	
@main.route('/portfolio_1_col')
def portfolio_1_col():
	return render_template('portfolio_1_col.html')

@main.route('/portfolio_2_col')
def portfolio_2_col():
	return render_template('portfolio_2_col.html')

@main.route('/portfolio_3_col')
def portfolio_3_col():
	return render_template('portfolio_3_col.html')

@main.route('/portfolio_4_col')
def portfolio_4_col():
	return render_template('portfolio_4_col.html')

@main.route('/portfolio_item')
def portfolio_item():
	return render_template('portfolio_item.html')

@main.route('/blog_home_1')
def blog_home_1():
	return render_template('blog_home_1.html')

@main.route('/blog_home_2')
def blog_home_2():
	return render_template('blog_home_2.html')

@main.route('/blog_post')
def blog_post():
	return render_template('blog_post.html')