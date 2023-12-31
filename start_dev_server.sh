yes | poetry run python /usr/matias_django_blog/matias_site/manage.py makemigrations
yes | poetry run python /usr/matias_django_blog/matias_site/manage.py migrate
yes | poetry run python /usr/matias_django_blog/matias_site/manage.py collectstatic --noinput
cd matias_site/
poetry run gunicorn -c config/gunicorn/config.py