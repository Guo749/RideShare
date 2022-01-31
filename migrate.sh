#!/bin/bash
while [ "1" = "1" ]
do 
    python manage.py makemigrations && python manage.py migrate && sleep 3
done