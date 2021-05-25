#!/usr/bin/env bash

echo "Build docker images......"
sudo docker build -t docker_react .

# Create Docker
echo "Run docker react_web......"
sudo docker run -it -d -p 80:3000 --name react_web docker_react

