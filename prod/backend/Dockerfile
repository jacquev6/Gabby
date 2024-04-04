FROM node:20 AS adapted-builder

WORKDIR /app

ADD adapted/package.json /app
ADD adapted/package-lock.json /app

RUN npm install

ADD adapted /app

RUN npx vite build


FROM python:3.12-slim as backend

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

COPY --from=adapted-builder /app/dist/index.html /app/textbooks/templates/adapted.html

ENV DJANGO_SETTINGS_MODULE=opinion.settings.prod
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
