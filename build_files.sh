#!/bin/bash

# Install pip if not available
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput
