#!/usr/bin/env bash

./manage.py migrate
./manage.py loaddata airline/fixtures/aircrafts.json
