#!/usr/bin/env bash

echo "Build docker images......"
sudo docker build -t twitter_transform .

# Create Docker
echo "Run docker twitter_tran......"
sudo docker run -d --name twitter_tran twitter_transform

