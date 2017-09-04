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
    upload_form = UploadForm()
    action_form = ActionForm()
    if 'upload' in request.form and upload_form.validate_on_submit() :
        filename = upload_form.text_file.data
        name = hashlib.md5(('admin' + str(time.time())).encode('UTF-8')).hexdigest()[:15]
        texts.save(filename, name=name + '.')
        file_path = texts.path(name + '.txt')
        input_info = subprocess.getoutput("cat %s"%file_path)
        action_form.input_text.data = input_info
        flash('Upload Success!')
        return render_template('index.html', upload_form=upload_form,action_form=action_form,output_flag = False)
    if 'action' in request.form and action_form.validate_on_submit():
        action_form.output_text.data = "Mission Complite!"
        return render_template('index.html', upload_form=upload_form,action_form=action_form,output_flag = True)
        
    return render_template('index.html', upload_form=upload_form,action_form=action_form,output_flag = False)


@main.route('/manage')
def manage_file():
    files_list = os.listdir(current_app.config['UPLOADED_TEXTS_DEST'])
    return render_template('manage.html', files_list=files_list)


@main.route('/open/<filename>')
def open_file(filename):
    file_url = texts.url(filename)
    return render_template('browser.html', file_url=file_url)

@main.route('/delete/<filename>')
def delete_file(filename):
    file_path = texts.path(filename)
    os.remove(file_path)
    return redirect(url_for('main.manage_file'))
    
# @main.route('/', methods=['GET', 'POST'])
# def index():
#     return render_template('index.html')
#     form = NameForm()
#     if form.validate_on_submit():
#         #user = User.query.filter_by(username=form.name.data).first()
#         #if user is None:
#         #    user = User(username=form.name.data)
#         #    db.session.add(user)
#         #    session['known'] = False
#         #    if current_app.config['FLASKY_ADMIN']:
#         #        send_email(current_app.config['FLASKY_ADMIN'], 'New User',
#         #                   'mail/new_user', user=user)
#         #else:
#         #    session['known'] = True
#         #session['name'] = form.name.data
#         return redirect(url_for('.index'))
#     return render_template('index.html',
#                            form=form, name=session.get('name'),
#                            known=session.get('known', False))




# @main.route("/users",methods=["GET"])
# def show_users():
#     total = current_app.config['USERS_COLLECTION'].find().count()
#     page, per_page, offset = get_page_items()
#     users_info = current_app.config['USERS_COLLECTION'].find({}).skip(offset).limit(per_page)
#     pagination = Pagination(page=page,per_page=per_page,total=total,css_framework='bootstrap3',record_name="UsersInfo")
#     start_pt = offset+1
#     end_pt = offset+per_page
#     if end_pt > total:
#         end_pt = total
#     pagination.display_msg = "Display %d-%d, Total %d" %(start_pt,end_pt,total)
#     return render_template('users.html', total = total,users=users_info,pagination=pagination)

# def get_page_items():
#     page = int(request.args.get('page', 1))
#     per_page = request.args.get('per_page')
#     if not per_page:
#         per_page = current_app.config.get('PER_PAGE', 2)
#     else:
#         per_page = int(per_page)

#     offset = (page - 1) * per_page
#     return page, per_page, offset

