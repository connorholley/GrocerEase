# Variables
LOCAL_USER='bert'          # PSQL user
LOCAL_PASS='guest'         # PSQL password
LOCAL_TEST_DB='testing-db'  # Testing DB
LOCAL_PROD_DB='production-db'  # Production DB

# Main Targets
all: setup

# Download the postgres Docker image and create the container with both databases.
setup:
	docker run -d \
		--name grocer-ease-psql \
		-p 5455:5432 \
		-e POSTGRES_USER='bert' \
		-e POSTGRES_PASSWORD='guest' \
		-e POSTGRES_DB='testing-db,production-db' \
		postgres

	# Sleep to allow PostgreSQL to start
	sleep 5

	# Create testing and production databases
	docker exec -i grocer-ease-psql createdb -U bert testing-db
	docker exec -i grocer-ease-psql createdb -U bert production-db

# Stop the container
down:
	docker stop grocer-ease-psql

# Remove the container
remove:
	docker rm grocer-ease-psql
