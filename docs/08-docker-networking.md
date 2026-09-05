# Docker Networking

## 1. What is a Docker Network
Docker network help containers or services communicate with each other.

## 2. Container-to-Container Communication
Container to container communication can use service name as a hostname if they are in same docker network.

## 3. Service Name as Hostname
We can use service name as hostname to reach another container if both containers are on the same docker network.

## 4. localhost in Docker
Localhost refer to current container or system we are inside.

## 5. Port Publishing
Port publishing is needed when we want to make container port accessible from outside docker network.

## 6. Host-to-Container vs Container-to-Container
Host to container require port mapping publish, while container to container communication does not require port mapping publishing when the container on the same docker network. Container to container can use service name as a hostname.

## 7. Docker Compose Network
Docker compose automatically create a network for the services, allowing the containers to communicate with each other.


## 8. docker compose down and Networks
Docker compose down basically will remove the containers and networks.