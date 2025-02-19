#!/bin/bash

# Ensure Python and pip are installed
export PATH="$HOME/.local/bin:$PATH"
python -m ensurepip --default-pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput
