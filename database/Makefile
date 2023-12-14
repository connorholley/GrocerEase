# Variables
LOCAL_USER='bert'          # PSQL user
LOCAL_PASS='guest'         # PSQL password
LOCAL_TEST_DB='testing-db'  # Testing DB
LOCAL_PROD_DB='production-db'  # Production DB

# Main Targets
all: setup-testing setup-production

# Download the postgres Docker image and create the testing container.
setup-testing:
	docker run -d \
		--name grocer-ease-psql-testing \
		-p 5455:5432 \
		-e POSTGRES_USER='bert' \
		-e POSTGRES_PASSWORD='guest' \
		-e POSTGRES_DB='testing-db' \
		postgres

# Download the postgres Docker image and create the production container.
setup-production:
	docker run -d \
		--name grocer-ease-psql-production \
		-p 5456:5432 \
		-e POSTGRES_USER='bert' \
		-e POSTGRES_PASSWORD='guest' \
		-e POSTGRES_DB='production-db' \
		postgres

# Stop the testing container
down-testing:
	docker stop grocer-ease-psql-testing

# Stop the production container
down-production:
	docker stop grocer-ease-psql-production

# Remove the testing container
remove-testing:
	docker rm grocer-ease-psql-testing

# Remove the production container
remove-production:
	docker rm grocer-ease-psql-production
