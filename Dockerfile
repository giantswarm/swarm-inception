FROM phusion/baseimage
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq && \
  apt-get install -y -q --no-install-recommends \
  python2.7 python-pip build-essential python-dev \
  git

RUN pip install Flask Flask-Cache requests redis

ADD server.py /app/server.py
ADD giantswarm.py /app/giantswarm.py
ADD github.py /app/github.py
ADD swarmconfig.py /app/swarmconfig.py

ENTRYPOINT ["python", "-u", "/app/server.py"]

EXPOSE 5000