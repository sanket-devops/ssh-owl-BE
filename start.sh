#!/bin/sh
export FLASK_APP=./app.py
pip run flask --debug run -h 0.0.0.0

#pipenv run flask --debug run -h 0.0.0.0