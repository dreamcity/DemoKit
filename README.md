# DemoKit
DemoKit With Flask


=======================================================================================
Deploy:
1. generate  the virtualenv config file 
	pip freeze > requirements.txt

2. update and install the virtualenv 
	pip install -r requirements.txt








Run:
1.Start redis-server
  1.1 annotation the bind 127.0.0.1 to enable the celery connection
  1.2 close the protected-mode, set protected-mode no
  1.3 run redis-server with redis.conf
      ./src/redis-server redis/conf

2.Start celery worker
  celery worker -A webapp.email.celery

3.Start cherrypy app
  ./server.py 
