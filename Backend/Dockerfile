# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt
COPY tw_cdb_credentials.py tw_cdb_credentials.py
COPY tweepy_code.py tweepy_code.py

RUN pip3 install -r requirements.txt

CMD [ "python3", "tweepy_code.py"]