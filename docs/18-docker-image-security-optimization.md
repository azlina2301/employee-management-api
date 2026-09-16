# security + optimization + caching

##Security

Running an application as a non-root user follows the principle of
least privilege. If the application is compromised, the attacker has
fewer privileges inside the container.

We can create a non-root user and then switch to that user:
```
RUN useradd --create-home appuser
```
```
USER appuser
```

USER appuser does not create the user; it tells Docker to run the
subsequent process as that user.

File ownership also matters. We can use:

```
COPY --chown=appuser:appuser . .
```

to make the copied files owned by appuser inside the image.

Secrets such as database passwords should not be baked into the
Dockerfile or image. They should be provided at runtime.

.dockerignore can exclude sensitive or unnecessary files such as
.env, .git, and __pycache__ from the Docker build context.


##Optimization
Using a smaller base image can reduce image size, storage usage,
and the amount of data that needs to be transferred.

For example:
```
FROM python:3.12
```
compared with:
```
FROM python:3.12-slim
```
python:3.12-slim generally contains fewer unnecessary packages and
is therefore smaller.


##Caching
Docker builds instructions layer by layer. Docker can reuse cached
layers when the relevant instruction and its inputs have not changed.

When a layer becomes invalid, Docker rebuilds that layer and the
subsequent layers.

Therefore, relatively stable instructions should generally come
before frequently changing instructions.

For example:
```
FROM python:3.12
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```