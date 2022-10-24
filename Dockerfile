FROM python:3.10-slim-buster

LABEL maintainer "Matias Cardenas"
LABEL description "Python 3.8 image containing Football Notifications APP"

USER root
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean \
&& apt-get install cron -y \
&& apt-get install bash \
&& apt-get install vim -y

RUN pip install poetry

WORKDIR /usr/matias_django_blog

COPY ./ ./

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN poetry install

CMD poetry run python /usr/matias_django_blog/matias_site/manage.py runserver 0.0.0.0:8000
