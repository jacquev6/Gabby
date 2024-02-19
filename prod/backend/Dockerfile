FROM python:3.12-slim

ADD backend /app

WORKDIR /app

RUN pip install -r requirements.txt

# @todo(Project management, soon) Run a production-ready version
ENV DJANGO_SETTINGS_MODULE=gabby.settings.prod
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
