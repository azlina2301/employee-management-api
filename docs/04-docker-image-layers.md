# Docker Image Layers

## 1. What is an Image Layer
Docker processes the instruction step by step in Dockerfile. With each instruction contributing to the image's layers.

## 2. Layer Caching
Each of the layer will be caching and reusable if no change happened.

## 3. Why Dockerfile Order Matters
If a layer changes, Docker generally rebuild that layer and subsequent layers. Therefore, frequently changing instruction should generally be placed later in the Dockerfile.

## 4. What Happens When Files Change
if app.py changed.
COPY requirements.txt → cached
RUN pip install       → cached
COPY . .              → rebuild
CMD                   → recreated/updated

if requirements.txt changed.
COPY requirements.txt → rebuild
RUN pip install       → rebuild
COPY . .              → rebuild
CMD                   → recreated/updated