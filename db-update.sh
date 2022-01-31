#!/bin/bash

while true
do
    python manage.py makemigrations 
    python manage.py migrate
    sleep 500 
done