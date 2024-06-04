FROM node:22 AS frontend-dependencies

WORKDIR /app

ADD frontend/package.json /app
ADD frontend/package-lock.json /app

# Work around https://github.com/npm/cli/issues/4828
RUN if [ $(uname --machine) = "aarch64" ]; then sed -i s/rollup-linux-x64-gnu/rollup-linux-arm64-gnu/g /app/package.json; fi

RUN npm install


FROM frontend-dependencies AS fontend-builder

ADD frontend /app
RUN cat src/promise-with-resolvers-polyfill.js node_modules/pdfjs-dist/build/pdf.worker.min.mjs >src/frontend/public/pdf.worker.min.js

ARG GABBY_VERSION
ENV VITE_OPINION_APP_VERSION=$GABBY_VERSION
ENV VITE_OPINION_APP_DEFAULT_LOCALE=fr
ENV GABBY_ENTRY_POINT_NAME=frontend

RUN npx vite build


FROM frontend-dependencies AS adapted-builder

ADD frontend /app
ENV VITE_OPINION_APP_DEFAULT_LOCALE=fr
ENV GABBY_ENTRY_POINT_NAME=adapted

RUN npx vite build

RUN test $(ls dist | wc -l) -eq 1


FROM python:3.12-slim AS backend-dependencies

RUN set -x \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends \
    postgresql-client \
 && true

WORKDIR /app

ADD backend/requirements.txt /app

RUN pip install -r requirements.txt


FROM python:3.12-slim AS doc-builder

WORKDIR /app

RUN pip install sphinx

ADD doc /app

ARG GABBY_VERSION
ENV GABBY_VERSION=$GABBY_VERSION

RUN sphinx-build -b html . build


FROM nginx:alpine AS final-frontend

RUN rm /etc/nginx/conf.d/default.conf
RUN rm /usr/share/nginx/html/*.html
ADD prod/docker/frontend.conf /etc/nginx/conf.d/frontend.conf
COPY --from=fontend-builder /app/dist /usr/share/nginx/html/frontend
COPY --from=doc-builder /app/build /usr/share/nginx/html/doc


FROM backend-dependencies AS final-backend

ADD backend /app

COPY --from=adapted-builder /app/dist/index.html /app/textbooks/templates/adapted.html

ENV DJANGO_SETTINGS_MODULE=opinion.settings.prod
CMD ["uvicorn", "gabby.asgi:app", "--host", "0.0.0.0", "--port", "80"]
