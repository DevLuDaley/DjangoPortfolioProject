release: python portfolio-project/manage.py migrate
web: gunicorn --env DJANGO_SETTINGS_MODULE=portfolio.settings portfolio.wsgi
