FROM python:3.12-slim

ADD backend /app

WORKDIR /app

RUN pip install -r requirements.txt

# @todo Run a production-ready version
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
