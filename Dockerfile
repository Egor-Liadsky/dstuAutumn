FROM ubuntu:latest
MAINTAINER Turtle Team 'Alexey Shashkin'
RUN apt-get update -qy
RUN apt -y upgrade
RUN apt install -y python3-pip
RUN pip install -r requirements.txt
CMD ["python3","main.py"]

