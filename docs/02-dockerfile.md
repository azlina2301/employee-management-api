# Dockerfile
Dockerfile is a template for creating new image.

## 1. FROM
The function of FROM is to get this base image to create new image.

## 2. WORKDIR
Set the current working directory for subsequent intructions and container processess.

## 3. COPY
Copy files from current build context into current working directory in image.

## 4. RUN
Execute the command during the image building.

## 5. CMD
Run the application during runtime.

## 6. Build Time vs Runtime
Build time basically happening start from Get the image till Run in order to build new image, and Runtime happeing during container start.