yes | poetry run python /usr/matias_django_blog/matias_site/manage.py makemigrations
yes | poetry run python /usr/matias_django_blog/matias_site/manage.py migrate
yes | poetry run python /usr/matias_django_blog/matias_site/manage.py collectstatic
cd matias_site/
poetry run gunicorn matias_site.wsgi --bind 0.0.0.0:8888 --workers 3 --daemon
nginx -g "daemon off;"