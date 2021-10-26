# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app
ENV format="web"
ENV port="5000"
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD python3 -u main.py $format -p $port