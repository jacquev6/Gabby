FROM node:20 AS builder

WORKDIR /app

ADD frontend/package.json /app
ADD frontend/package-lock.json /app

RUN npm install

ADD frontend /app
RUN cp node_modules/pdfjs-dist/build/pdf.worker.min.mjs public/pdf.worker.min.js

ARG GABBY_VERSION
ENV VITE_GABBY_VERSION=$GABBY_VERSION

RUN npx vite build


FROM nginx:alpine AS final

COPY --from=builder /app/dist /usr/share/nginx/html
