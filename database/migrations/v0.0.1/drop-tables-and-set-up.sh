#!/bin/bash

# Common PostgreSQL connection parameters
PG_USER="bert"
PG_PASSWORD="guest"
PG_CONTAINER="grocer-ease-psql"

# Function to apply SQL script to a database
apply_sql_script() {
    local DB_NAME="$1"
    local SQL_SCRIPT="$2"
    
    docker exec -i "$PG_CONTAINER" psql -U "$PG_USER" -d "$DB_NAME" < "$SQL_SCRIPT" >/dev/null 2>&1
}


# List of databases for apply
APPLY_DATABASES=("testing-db")
APPLY_SQL_SCRIPT="apply.sql"

# List of databases for rollback
ROLLBACK_DATABASES=("testing-db")
ROLLBACK_SQL_SCRIPT="roll-back.sql"


# Rollback SQL script for each database
for DB_NAME in "${ROLLBACK_DATABASES[@]}"; do
    apply_sql_script "$DB_NAME" "$ROLLBACK_SQL_SCRIPT"
done


# Apply SQL script to each database
for DB_NAME in "${APPLY_DATABASES[@]}"; do
    apply_sql_script "$DB_NAME" "$APPLY_SQL_SCRIPT"
done
