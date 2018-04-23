FROM debian
LABEL maintainer "Marco De Donno <Marco.DeDonno@unil.ch>"

RUN apt update && \
    apt upgrade -y

################################################################################
###   Python

RUN apt install -y python python-pip python-dev \
    build-essential libssl-dev libffi-dev libpq-dev
RUN pip install --upgrade pip

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

################################################################################
###   MDmisc library

COPY ./ /MDmisc

RUN echo /MDmisc/ > /usr/local/lib/python2.7/dist-packages/mdedonno.pth

WORKDIR /MDmisc

################################################################################
###   Unit test by default

RUN python /MDmisc/doctester.py
