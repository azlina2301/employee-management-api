# Docker Fundamentals

Docker is a platform/tool for building, running, and managing containers.

## 1. Docker Image vs Container

An image is a blueprint/template used to build a container. A container is an instance created from an image that runs applications or processes.

## 2. Running vs Stopped Container

We can see which containers are currently running using `docker ps`. To see all containers, including running and stopped containers, we can use `docker ps -a`.

## 3. Port and Listening

A port can be defined as a numbered network endpoint. Listening means that an application is waiting for incoming network connections or requests on a port.

## 4. Port Mapping

Port mapping allows applications on the host (such as your Mac) to communicate with a container through a published port. It is not necessary for communication between containers on the same Docker network.

## 5. localhost

`localhost` refers to the environment that we are currently working in.

## 6. Docker Network

A Docker network allows containers to communicate with each other. In Docker Compose, containers can use a service name as a hostname to reach another container on the same network, such as `postgres-db:5432`.

## 7. EXPOSE

`EXPOSE` declares the port that the application in the image is intended to use. It does not make the application listen on that port or create a host port mapping.

## 8. CMD vs ENTRYPOINT

`ENTRYPOINT` defines the main executable or program, while `CMD` provides the default argument. An argument provided after the image name can replace the default `CMD` argument.

## 9. Docker Volumes

Docker volumes are primarily used to ensure data persistence independent of the container lifecycle.

## 10. Named Volume vs Bind Mount

A named volume is managed by Docker, while a bind mount uses a file or directory from the local computer.