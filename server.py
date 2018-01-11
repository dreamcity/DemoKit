#!/usr/bin/env python
import time, sys, cherrypy, os
#from paste.translogger import TransLogger
from webapp import create_app

def run_server(app): 
    # Enable WSGI access logging via Paste
    #app_logged = TransLogger(app)
 
    # Mount the WSGI callable object (app) on the root directory
    cherrypy.tree.graft(app, '/')
 
    # Set the configuration of the web server
    cherrypy.config.update({
	#'engine.autoreload.on': True,
        #'log.access_file': 'site.log',
	#'log.screen': True,
        'server.socket_port': 5000,
        'server.socket_host': '192.168.0.183'
        #'server.socket_host': '127.0.0.1'
    })
 
    # Start the CherryPy WSGI web server
    cherrypy.engine.start()
    cherrypy.engine.block()

if __name__ == '__main__':
	app = create_app()
	run_server(app)


