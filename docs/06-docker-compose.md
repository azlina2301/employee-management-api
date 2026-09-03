# Docker Compose

## 1. What is Docker Compose
Docker compose is a tool for defining and managing multiple services that make up an application.

## 2. Services
A service define how a container should be created and run. A compose application can have multiple services.

## 3. build vs image
image specificies the existing image to use, while build tell the docker compose to build an image using dockerfile and build context.

## 4. Service Name and Docker Network
A service name can be used as a hostname for container-to-container communication within the same Docker network.

## 5. Port Mapping
port mapping map host port to container port so application outside the container can communicate with it.

## 6. depends_on
depends_on defines a startup dependency between services and controls their startup order.

## 7. docker compose up
docker compose up build an image when needs. create the required container and network. start the service.

## 8. docker compose down
docker compose down stops and removes the containers and networks created by Compose while normally keeping named volumes.

## 9. Docker Compose and Volumes
Volumes are used for data persistence independently of the container lifecycle.