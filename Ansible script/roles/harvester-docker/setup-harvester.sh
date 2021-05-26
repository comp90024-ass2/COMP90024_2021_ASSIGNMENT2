#!/usr/bin/env bash

cd harvester

echo "Build docker images......"
sudo docker build -t twitter_harvester .

# Create Docker
echo "Run docker twitter_harv......"
sudo docker run -d --name twitter_harv twitter_harvester

