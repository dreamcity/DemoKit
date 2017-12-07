# -*- coding: utf-8 -*-

from flask import render_template,request,flash

from . import main

#Data Analysis--------------------------------------------------------
@main.route('/data_analysis')
def data_analysis():
	return render_template('data_analysis.html',sub_item = 0)

@main.route('/data_analysis/processing')
def data_processing():
	return render_template('data_analysis.html',sub_item = 1)

@main.route('/data_analysis/digging')
def data_digging():
	return render_template('data_analysis.html',sub_item = 2)

@main.route('/data_analysis/statistics')
def data_statistics():
	return render_template('data_analysis.html',sub_item = 3)

@main.route('/data_analysis/visualization')
def data_visualization():
	return render_template('data_analysis.html',sub_item = 4)
#--------------------------------------------------------------------
