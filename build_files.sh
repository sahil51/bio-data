#!/bin/bash
# Ensure Python and pip are available
which python3 || exit 1
which pip3 || exit 1

# Install dependencies
pip3 install --upgrade pip
pip3 install -r requirements.txt

# Run migrations and collect static files
python3 manage.py migrate
python3 manage.py collectstatic --noinput
