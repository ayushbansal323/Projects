#! /bin/sh
sudo apt install git \
&& sudo apt install git --upgrade \
&& sudo apt install python3-pip \
&& sudo apt install --upgrade python3-pip \
&& pip3 install --upgrade google-api-python-client \
&& pip3 install oauth2client \
&& pip3 install --upgrade oauth2client \
&& pip3 install bs4 \
&& pip3 install --upgrade bs4 \
&& pip3 install python-dateutil \
&& pip3 install --upgrade python-dateutil \
&& pip3 install matplotlib \
&& pip3 install sklearn \
&& pip3 install --upgrade sklearn \
&& pip3 install Django==2.1.2 \
&& sudo apt-get install sqlite3 libsqlite3-dev 
