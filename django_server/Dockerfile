FROM python:3.10.4-alpine

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

# install psycopg dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

CMD
