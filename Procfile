:release python manage.py makemigrations --noinput
:release python manage.py migrate --noinput
:release python manage.py collectstatic --noinput

web: gunicorn mysite.wsgi