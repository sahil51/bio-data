#!/bin/bash

# Ensure pip is installed
python -m ensurepip --default-pip

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# Run migrations (optional, if needed)
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput
