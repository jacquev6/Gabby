FROM python:3.12-slim

RUN set -x \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends \
    postgresql-client \
 && true

WORKDIR /app

ADD backend/requirements.opinion.txt /app

RUN pip install -r requirements.opinion.txt

ADD backend/requirements.app.txt /app

RUN pip install -r requirements.app.txt

ADD backend /app

ENV DJANGO_SETTINGS_MODULE=opinion.settings.prod
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
