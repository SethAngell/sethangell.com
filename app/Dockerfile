FROM python:3.9.5-slim-buster

# Set working directory for all following in container commands
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DB_ENGINE django.db.backends.postgresql_psycopg2
ENV DB_NAME postgres
ENV DB_USER postgres
ENV DB_PASS bad_password
ENV DB_HOST "db"
ENV DB_PORT 5432

RUN apt-get update \
  && apt-get -y install gcc postgresql libpq-dev vim \
  && apt-get clean

# Handle all necessary dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Install App
COPY . .

RUN python manage.py makemigrations

ENTRYPOINT (python manage.py migrate && python manage.py runserver 0.0.0.0:8000)