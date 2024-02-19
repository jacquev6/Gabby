FROM node:20

ADD frontend /app

WORKDIR /app

ADD frontend/package.json /app
ADD frontend/package-lock.json /app

RUN npm install

ADD frontend /app
RUN cp node_modules/pdfjs-dist/build/pdf.worker.min.mjs public/pdf.worker.min.js

ARG GABBY_VERSION
ENV VITE_GABBY_VERSION=$GABBY_VERSION

# @todo(Project management, soon) Run a production-ready version
CMD ["npx", "vite", "--host", "0.0.0.0", "--port", "80", "--strictPort"]
