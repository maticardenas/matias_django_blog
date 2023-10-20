FROM python:3.10-slim-buster

LABEL maintainer "Matias Cardenas"
LABEL description "Python 3.8 image containing Football Notifications APP"

USER root
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean \
&& apt-get install bash \
&& apt-get install vim -y \
&& apt-get -y install libpq-dev gcc \
&& apt-get -y install nginx \
&& apt-get -y install procps

RUN pip install poetry

WORKDIR /usr/matias_django_blog

COPY ./ ./
COPY nginx.conf /etc/nginx/conf.d/default.conf

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN poetry install
