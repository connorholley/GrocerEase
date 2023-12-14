#!/bin/bash

# SQL script file
SQL_SCRIPT="apply.sql"

# List of databases
DATABASES=("testing-db" "production-db")

# PostgreSQL connection parameters
PG_USER="bert"
PG_PASSWORD="guest"
PG_CONTAINER="grocer-ease-psql"

# Iterate over each database and execute the SQL script
for DB_NAME in "${DATABASES[@]}"; do
    echo "Applying SQL script to database: $DB_NAME"
    docker exec -i "$PG_CONTAINER" psql -U "$PG_USER" -d "$DB_NAME" < "$SQL_SCRIPT"
done
