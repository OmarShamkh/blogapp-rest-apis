# defines base image
FROM python:3.10.6

# create working directory for app
WORKDIR /app

# installs required modules/dependencies 
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt 

# copy app files to the working directory
COPY . .

# forward the request from port 8000 on the host to port 8000 in the container
EXPOSE 8000

# run app 
CMD python3 manage.py runserver 0.0.0.0:8000