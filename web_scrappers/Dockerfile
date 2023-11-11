FROM ubuntu:latest

WORKDIR /usr/src/app

# prevent Python from writing .pyc files
ENV PYTHONDOWNWRITEBYTECODE 1

#ensure Python is sent directly to the terminal without buffering
ENV PYTHONBUFFERED 1

RUN apt-get update
RUN apt-get install -y python3-pip

# Install Chrome
# RUN apt-get install -y wget
# RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# # Install necessary tools
# RUN apt-get update && apt-get install -y wget unzip

# # Download Chrome
# RUN wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.105/linux64/chrome-linux64.zip

# # Unzip the downloaded file
# RUN unzip chrome-linux64.zip

# # Move the unzipped directory to /opt/google/chrome
# RUN mv chrome-linux64 /usr/local/bin/chrome



# # Install Chromedriver
# RUN apt-get install -yqq unzip
# RUN wget -O /tmp/chromedriver.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.105/linux64/chromedriver-linux64.zip
# RUN unzip /tmp/chromedriver.zip -d /usr/local/bin/


COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh
COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

