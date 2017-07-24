#!/usr/bin/env python
import os
from flask_script import Manager
from webapp import create_app

if __name__ == '__main__':
	app = create_app()
	manager = Manager(app)
	manager.run()
