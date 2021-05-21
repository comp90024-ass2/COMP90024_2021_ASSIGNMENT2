#!/usr/bin/env bash

echo "Build docker images......"
sudo docker build -t twitter_harvester .

# Create Docker
echo "Run docker couchDB......"
sudo docker run -d --name twitter_harv twitter_harvester

