# Lesson 17 - Docker Security

## Root user

Running an application as the root user can increase the security risk of a container.

If an attacker exploits a vulnerability in the application, they may gain the same privileges as the user running the application. If the application is running as root, the attacker may have higher privileges inside the container.

Therefore, it is better to run the application as a non-root user when possible.

## USER

`USER` tells Docker which user should run the application and subsequent processes.

For example:

```dockerfile
USER appuser
```

This means the application will run as `appuser` instead of root.

However, `USER` does not create the user automatically. The user must already exist in the image.

## File permissions

When running the application as a non-root user, we need to make sure that the user has the required permissions to access the application files.

If the application needs to write to a specific directory, we should give the application user permission to write only to that directory.

This follows the principle of **least privilege**:

> Give the application only the permissions it needs.

## COPY --chown

`COPY --chown` can be used to set the ownership of files when copying them into the image.

Example:

```dockerfile
COPY --chown=appuser:appuser . .
```

This makes `appuser` the owner of the copied files inside the image.

## Secrets

We should not put passwords or other secrets directly into the Dockerfile.

For example, we should avoid:

```dockerfile
ENV DB_PASSWORD=mysecretpassword
```

Secrets can potentially become part of the image configuration or build history.

Instead, sensitive configuration should be provided at runtime, such as through environment variables.

## .env and .gitignore

A `.env` file can contain sensitive configuration such as passwords.

Adding `.env` to `.gitignore` helps prevent the file from being committed to Git.

However, `.gitignore` does not guarantee that the secret is safe.

If a secret has already been committed or exposed, adding the file to `.gitignore` does not remove the secret from Git history. The exposed credential should be rotated or revoked.
