# Docker Compose Volumes

## 1. Why Use Volumes in Compose
Volumes provide data persistence. Without a volume, when Compose removes the container, data stored in the container is also removed.

## 2. Declaring a Named Volume
volumes:
    postgres-data:

## 3. Mounting a Volume
services:
    postgres-db:
        volumes:
            - postgres-data:/var/lib/postgresql/data

## 4. Volume and Container Lifecycle
volume and container lifecycle is independent to each other.

## 5. docker compose down vs down -v
docker compose down removes the containers without removing the named volumes, while docker compose down -v removes both the containers and volumes.

## 6. Automatic Volume Creation
Compose automatically creates the named volume if it is declared in the Compose file and does not already exist.

## 7. Reusing an Existing Volume
When docker compose up runs again, Compose can reuse the existing named volume and mount it to the newly created container.