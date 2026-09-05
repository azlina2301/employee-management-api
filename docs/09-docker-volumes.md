# Docker Volumes

## 1. Why Do We Need Volumes
The main purpose of the volume is data persistence.

## 2. Container Data vs Persistent Data
Container data will be removed when the container is removed. In order to persist the data, we can create a volume which is independent of the container.

## 3. Named Volumes
Named volumes is managing by docker.

## 4. Mounting a Volume
Mounting a volume allows a container to use the volume for data storage.

## 5. Bind Mounts
A bind mount uses a local directory or path on the host to store data.

## 6. Named Volume vs Bind Mount
Named volumes are managed by Docker, while bind mounts use a local directory or path on the host. Bind mounts are useful during development because they provide direct access to host files.

## 7. Volume and Container Lifecycle
The volume and container lifecycles are independent of each other.