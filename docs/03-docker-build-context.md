# Docker Build Context

## 1. What is Build Context
Build context is directory/path provided to docker build, containing the files Docker can access during the build.

## 2. docker build .
The . specify the current directory as the build context and tell the Docker to build an image using that context.

## 3. COPY and Build Context
Copy get the file from build context.

## 4. .dockerignore
.dockerignore is used to exclude unnecessary or sensitive file from the build context, such as crendential or large files that aren't needed for the build.