FROM tiangolo/meinheld-gunicorn-flask:python2.7

MAINTAINER Ben Willett "benw@techcamp.com.au"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN git clone https://github.com/benjaminwillett/houseprices.git

WORKDIR /app/houseprices

COPY . /app

WORKDIR /app

RUN ls

RUN pip install -r requirements.txt



