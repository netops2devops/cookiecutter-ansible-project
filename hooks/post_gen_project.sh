#!/bin/bash

echo "creating virtualenv and installing requirements"
python3 -m venv venv
source venv/bin/activate
pip3 install -U pip
pip install -r requirements.txt
deactivate