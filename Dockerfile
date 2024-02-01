FROM python:3.7-alpine3.7

RUN mkdir /app

COPY requirements.txt /app

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip3 install --upgrade pip


RUN apk add build-base openldap-dev python3-dev libffi-dev python-dev postgresql-dev
RUN pip3 install Cmake

RUN pip3 install postgres
RUN pip3 install psycopg2-binary
RUN pip3 install psycopg2
RUN pip3 install -r /app/requirements.txt --no-cache-dir


COPY picasso/ /app

WORKDIR /app