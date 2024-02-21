FROM python:3.12-slim

WORKDIR /app

RUN pip install gunicorn

ADD backend/requirements.txt /app

RUN pip install -r requirements.txt

ADD backend /app

ENV DJANGO_SETTINGS_MODULE=gabby.settings.prod
CMD ["gunicorn", "gabby.wsgi:application", "--bind", "0.0.0.0:80"]
