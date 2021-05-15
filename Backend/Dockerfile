# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

ENV HTTP_PROXY http://wwwproxy.unimelb.edu.au:8000
ENV HTTPS_PROXY http://wwwproxy.unimelb.edu.au:8000
ENV NO_PROXY localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.unimelb.edu.au,.cloud.unimelb.edu.au


COPY requirements.txt requirements.txt
COPY tw_cdb_credentials.py tw_cdb_credentials.py
COPY harvester_search_allcities.py harvester_search_allcities.py

RUN pip3 install -r requirements.txt

CMD [ "python3", "harvester_search_allcities.py"]