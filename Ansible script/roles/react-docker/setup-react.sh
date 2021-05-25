#!/usr/bin/env bash

cd COMP90024_2021_ASSIGNMENT2/Frontend/assignment2-map

echo "Build docker images......"
sudo docker build -t docker_react .

# Create Docker
echo "Run docker react_web......"
sudo docker run -it -d -p 80:3000 --name react-web docker_react:latest

