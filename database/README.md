# Database

This project uses PostgreSQL as it's primary database. This folder provides a simple way of running the database
locally, and maintains migration scripts for each version of the database.

# Running Locally

To run this program locally, ensure you have `docker` and `make` installed and available in your terminal. Everything is managed via `make`, so:

```bash
make setup
```

Will download the official postgres docker image & create a docker container.

```bash
make up
```

Will run the container (accesible via port 5432 on localhost).

```bash
make down
```

Will stop the container. Note: running `make down` and then `make up` (maybe the next day) will not cause the
database to lose any data.

```bash
make rm
```

Will delete the container.

# Migration Scripts

navigate to the migrations folder and run ./apply.sh to run the necessary table creates

In order to access the docker postgresql run:
`    docker exec -it grocer-ease-psql bash
   `
Once within this run
```
psql -U bert -d testing-db

    ```

From here we can view tables
