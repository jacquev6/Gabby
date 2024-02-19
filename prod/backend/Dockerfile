FROM python:3.12-slim

WORKDIR /app

ADD backend/requirements.txt /app

RUN pip install -r requirements.txt

ADD backend /app

# @todo(Project management, soon) Serve with an actual production-ready server (Gunicorn?)
ENV DJANGO_SETTINGS_MODULE=gabby.settings.prod
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
