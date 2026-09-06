# Docker Image Tags and Registry

## 1. Image Name and Tag
for example: postgres:17, postgres is the image/repository while 17 is the tag.

## 2. latest Tag
latest is the default tag when no tag is specify.

## 3. Version Tags
Version tags are useful when we encounter bug in the newer version because we can roll back to the previous version.

## 4. Tags vs Images
A tag is label/reference that points to an image. Multiple tags can point to the same underlying image.

## 5. docker tag
docker tag create another tag/reference for an existing image. It can be used for versioning or to add registry/repository name before pushing.

## 6. Container Registry
Container registry is a place where the container images are stored and distributed. Docker hub is an example of container registry.

## 7. docker pull
docker pull download an image from container registy to the local docker environment.

## 8. docker push
docker push upload an image to the container registry.