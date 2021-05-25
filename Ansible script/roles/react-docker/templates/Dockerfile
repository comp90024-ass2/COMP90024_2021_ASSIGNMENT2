# syntax=docker/dockerfile:1

FROM node:13.12.0-alpine as build-deps

ENV HTTP_PROXY http://wwwproxy.unimelb.edu.au:8000
ENV HTTPS_PROXY http://wwwproxy.unimelb.edu.au:8000
ENV NO_PROXY localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.necta>

# set working directory
WORKDIR /app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json ./
COPY package-lock.json ./

RUN npm install

COPY . ./


EXPOSE 3000
# start app
CMD ["npm", "start"]