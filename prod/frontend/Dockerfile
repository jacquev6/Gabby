FROM node:20

ADD frontend /app

WORKDIR /app

RUN npm install
RUN cp node_modules/pdfjs-dist/build/pdf.worker.min.mjs public

ARG GABBY_VERSION
ENV VITE_GABBY_VERSION=$GABBY_VERSION

# @todo Run a production-ready version
CMD ["npx", "vite", "--host", "0.0.0.0", "--port", "80", "--strictPort"]
