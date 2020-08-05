web: gunicorn --chdir web_server/ web_server.wsgi -b :$PORT
release: python web_server/manage.py migrate
