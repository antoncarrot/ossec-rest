FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN adduser -D ossec_rest

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && apk add postgresql-client \
    && pip install psycopg2 \
    && apk del build-deps

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r ./requirements.txt && pip install gunicorn

USER ossec_rest
CMD gunicorn config.wsgi:application --bind 0.0.0.0:8080
