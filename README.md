#flask-celery

#linux

gunicorn -c gun.conf manager:app
celery worker -B -A  manager.celery -l info

http://localhost:8866

