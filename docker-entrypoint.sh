#!/usr/bin/env bash

echo 'Collecting static files...'
python manage.py collectstatic --noinput

echo 'Migrate DB...'
python manage.py migrate --noinput

echo 'Starting server...'
python manage.py runserver 0.0.0.0:8000 --nostatic
