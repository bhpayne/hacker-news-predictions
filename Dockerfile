# https://github.com/phusion/baseimage-docker
# https://hub.docker.com/r/phusion/baseimage/tags
FROM phusion/baseimage:0.11

RUN apt-get update && \
    apt-get install -y \
# text editing
               vim \
# python 3
               python3 \
               python3-pip \
               python3-dev \
    && rm -rf /var/lib/apt/lists/*
    
RUN echo "alias python=python3" > /root/.bashrc

# https://docs.docker.com/engine/reference/builder/#copy
# requirements.txt contains a list of the Python packages needed for the PDG
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

RUN useradd --create-home appuser
WORKDIR       /home/appuser/app
USER appuser
 
