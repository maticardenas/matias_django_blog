yes | poetry run python /usr/matias_django_blog/matias_site/manage.py makemigrations
yes | poetry run python /usr/matias_django_blog/matias_site/manage.py migrate
poetry run python /usr/matias_django_blog/matias_site/manage.py runserver 0.0.0.0:8888