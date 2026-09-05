# Dockerfile + Environment Variables

## 1. ENV in Dockerfile
ENV in dockerfile define default environment variable.

## 2. Environment Variables as Defaults
Environment variables can be declared in dockerfile using ENV and provide default values.

## 3. Overriding with docker run -e
docker run -e can override the default environment variable in the Dockerfile during container runtime.

## 4. Overriding with Docker Compose
Docker Compose environment can override the default environment variable in the Dockerfile during container runtime.

## 5. .env and Compose
.env is a file that stores environment variables. Compose can read values from .env and substitute them into the Compose configuration.

## 6. .gitignore and Secrets
.gitignore helps prevent sensitive files from being committed to Git, such as files containing passwords or API keys.

## 7. Important Security Note
Sensitive files should be added to .gitignore before committing. If a secret has already been committed, adding the file to .gitignore does not remove it from Git history, so the exposed credential should be rotated or revoked.