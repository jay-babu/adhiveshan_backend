release: python manage.py makemigrations && python manage.py migrate
web: newrelic-admin run-program gunicorn adhiveshan_backend.wsgi
