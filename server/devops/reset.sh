#!/usr/bin/env bash

PGPASSWORD=postgres psql -h 127.0.0.1 -p 5432 -U postgres -c "DROP DATABASE airline_db;"
PGPASSWORD=postgres psql -h 127.0.0.1 -p 5432 -U postgres -c "CREATE DATABASE airline_db;"
PGPASSWORD=postgres psql -h 127.0.0.1 -p 5432 -U postgres -c "GRANT ALL ON DATABASE airline_db TO airline;"
