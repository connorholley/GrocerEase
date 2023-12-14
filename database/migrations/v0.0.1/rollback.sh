#!/bin/bash

# SQL script file
SQL_SCRIPT="rollback.sql"

# PostgreSQL connection parameters
PG_USER="bert"
PG_PASSWORD="guest"
PG_CONTAINER="grocer-ease-psql"

# Execute the SQL script
echo "Executing SQL script: $SQL_SCRIPT"
docker exec -i "$PG_CONTAINER" psql -U "$PG_USER" -f "$SQL_SCRIPT"
