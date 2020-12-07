## Overview ##
Please refer to the VitaInstant Final Report for more details. 

This API was created for project Vitainstant.
VitaInstant is a prototypical medication/supplement 
dispenser device made for CSULB's senior project course.
This API is based on micro-service architecture, as 
creating smaller services allow for faster run times.
As of now the the API only has SMS & SMTP Email Services

## Server ##
The API is served on an Ubuntu 18.04 server launched with 
Amazon AWS ECS2 services. 

## Flask ##
Flask is great for serving micro-service based API's.
Comparable to Django. This is where we encapsulate the 
SMS/Email models and where we serve the API.

## Docker ##
Docker is used containerize objects to be launched on 
different machines. Allows for scabillity and cloud
computing. 

## uWSGI ##
Main web server that opens up the sockets where the web
requests are being passed into. Interacts with 
NGINX using uwsgi. 

## NGINX ## 
In this case I use NGINX as a Reverse Proxy to 
pass Web Requests to the uWSGI server. 

## INSTALL DOCKER ON UBUNTU ##
sudo apt-get update 
sudo apt install docker.io
sudo chmod 666 /var/run/docker.sock

