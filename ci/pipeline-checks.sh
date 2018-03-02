#!/usr/bin/env sh

echo 'Verifying migrations have been made...'
python webapp/manage.py makemigrations --check

echo 'Checking linter status...'
pylint webapp/geek_text
pylint webapp/book_details
pylint webapp/browse
pylint webapp/reviews

echo 'Running Django tests...'
python webapp/manage.py test

echo 'Done!'

