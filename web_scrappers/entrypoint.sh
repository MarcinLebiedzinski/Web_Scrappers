#!/bin/bash
echo "Apply database migrations"
python3 manage.py migrate

exec "$@"