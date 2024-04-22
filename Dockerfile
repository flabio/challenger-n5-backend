FROM python:3.10.4-alpine3.15
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
WORKDIR /app


COPY requirements.txt /app/

RUN python3 -m pip install -r requirements.txt

COPY . /app/
