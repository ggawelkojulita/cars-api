#!/usr/bin/env sh

gunicorn api.wsgi:application --bind=0.0.0.0:8000 --workers=4 --timeout=3600 --reload --access-logfile -
