FROM python:3.7-alpine
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk upgrade
RUN apk add gcc python3-dev musl-dev postgresql-dev build-base jpeg-dev zlib-dev bash curl
RUN pip install --upgrade pip

COPY ./requirements.txt .
COPY . .

RUN pip install -r requirements.txt --upgrade
RUN python manage.py collectstatic --noinput

RUN adduser -D djangouser
USER djangouser