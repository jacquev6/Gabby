FROM node:20

ADD frontend /app

WORKDIR /app

RUN npm install

ARG GABBY_VERSION
ENV VITE_GABBY_VERSION=$GABBY_VERSION

# @todo RUn a production-reday version
CMD ["npm", "run", "dev"]
