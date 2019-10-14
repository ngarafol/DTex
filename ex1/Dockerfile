FROM ubuntu:xenial
MAINTAINER ngarafol@gmail.com

RUN \
  apt-get update && \
  apt-get -y upgrade && \
  DEBIAN_FRONTEND=noninteractive \
  apt-get install -y software-properties-common && \
  apt-get install -y build-essential && \
  apt-get install -y python3-pip 

RUN useradd -m noob
USER noob
WORKDIR /home/noob

COPY --chown=noob:noob requirements.txt requirements.txt

RUN pip3 install --user -r requirements.txt

COPY --chown=noob:noob ./getweather.py /home/noob/getweather.py

ENV HOME /home/noob

CMD ["python3", "./getweather.py"]
