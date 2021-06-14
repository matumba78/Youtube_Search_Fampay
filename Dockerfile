FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /video_Search
WORKDIR /video_Search

ADD . /video_Search

COPY ./requirements.txt /video_Search/requirements.txt

RUN pip install -r requirements.txt

COPY . /video_Search
