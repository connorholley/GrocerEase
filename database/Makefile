# Variables
LOCAL_USER='bert'          # PSQL user
LOCAL_PASS='guest'         # PSQL pasword
LOCAL_DB='grocer-ease-db'  # Primary DB


# Main Target
all: setup up

# Download the postgres Docker image and create the
# container.
setup:
	docker pull postgres
    docker create \
	--name grocer-ease-psql \
	-p 5455:5432 \
	-e POSTGRES_USER=$(LOCAL_USER) \
	-e POSTGRES_PASSWORD=$(LOCAL_PASS) \
    -e POSTGRES_DB=$(LOCAL_DB) \
    -d \
    postgres

# Run an existing container
up:
	docker start grocer-ease-psql 

# Stop a running container
down:
	docker stop grocer-ease-psql

# Remove an existing container
remove:
	docker rm grocer-ease-psql
