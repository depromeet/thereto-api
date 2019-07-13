#!/bin/bash

if [[ -z "${PROJECT_ENV}" ]]; then
  export $(cat .env | xargs)
fi

python manage.py runserver
