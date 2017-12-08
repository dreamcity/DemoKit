# -*- coding: utf-8 -*-
import os
import sys
import time
import hashlib
import subprocess
import json
# from flask import render_template, session, redirect, url_for, current_app
# from flask import Flask,current_app,render_template,request,redirect,url_for,session,flash
from flask import render_template,request,flash
#from flask.ext.paginate import Pagination
# from flask_paginate import Pagination
from flask_login import current_user


#from ..email import send_email
from . import main
from .forms import UploadForm, ActionForm
from .. import texts

sys.path.append("../../")
from webengine.classification import nlplib

#Machine Learning----------------------------------------------------
@main.route('/machine_learning')
def machine_learning():
	return render_template('machine_learning.html')

@main.route('/machine_learning/cluster')
def cluster():
	return render_template('cluster.html')

@main.route('/machine_learning/classify')
def classify():
	return render_template('classify.html')

@main.route('/machine_learning/classify/nlp', methods=['GET', 'POST'])
def classify_nlp():
	upload_form = UploadForm()
	action_form = ActionForm()
	# print("request_form",request)
	if 'upload' in request.form and upload_form.validate_on_submit() :
		if current_user.is_anonymous:
			sub_storage_id = "None"
		else :
			sub_storage_id = str(current_user.user_id)

		filename = upload_form.text_file.data
		name = hashlib.md5(('admin' + str(time.time())).encode('UTF-8')).hexdigest()[:15]
		texts.save(filename,  folder=sub_storage_id, name=name + '.')
		file_path = texts.path(sub_storage_id+"/"+name + '.txt')
		# print("file_path: ",file_path)
		input_info = subprocess.getoutput("cat %s"%file_path)
		action_form.input_text.data = input_info
		flash('Upload Success!')


		file_md5info = subprocess.getoutput("md5sum %s"%file_path).split()[0]

		if False:
			#替换为查找数据库，如果数据库中存在，则删除，即不保存
			os.remove(file_path)
		else:
			os.rename(file_path,os.path.split(file_path)[0]+"/%s.txt"%file_md5info)
			# print("new_file: ",os.path.split(file_path)[0]+"/%s.txt"%file_md5info)
		return render_template('nlp.html', upload_form=upload_form,action_form=action_form,output_flag = False)
	
	if 'action' in request.form and action_form.validate_on_submit():
		action_form.output_text.data = nlplib.NLP().words_split(action_form.input_text.data)
		return render_template('nlp.html', upload_form=upload_form,action_form=action_form,output_flag = True)

	return render_template('nlp.html', upload_form=upload_form,action_form=action_form,output_flag = False)

@main.route('/machine_learning/classify/ann', methods=['GET', 'POST'])
def classify_ann():
	action_form = ActionForm()
	if 'action' in request.form and action_form.validate_on_submit():
		action_form.output_text.data = action_form.input_text.data
		# base_json = json.dumps(action_form.input_text.data)
		base_json = action_form.input_text.data
		print("base_json",base_json)
		return render_template('ann.html', action_form=action_form,base_json = base_json)

	return render_template('ann.html', action_form=action_form)


@main.route('/machine_learning/predict')
def predict():
	return render_template('predict.html')