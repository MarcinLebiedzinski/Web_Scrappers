FROM selenium/standalone-chrome:latest

WORKDIR /usr/src/app

# prevent Python from writing .pyc files
ENV PYTHONDOWNWRITEBYTECODE 1

#ensure Python is sent directly to the terminal without buffering
ENV PYTHONBUFFERED 1

USER root
RUN apt-get update && apt-get install -y python3-pip

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/

