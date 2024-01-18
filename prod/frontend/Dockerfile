FROM node:20

ADD frontend /app

WORKDIR /app

RUN npm install

ARG GABBY_VERSION
ENV VITE_GABBY_VERSION=$GABBY_VERSION

# @todo Run a production-ready version
CMD ["npm", "run", "dev"]
