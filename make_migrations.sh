#! /bin/bash

python manage.py makemigrations users
python manage.py makemigrations students
python manage.py makemigrations teachers
python manage.py makemigrations courses
python manage.py makemigrations qualifications

python manage.py migrate