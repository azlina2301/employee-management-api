from python:3.12

WORKDIR /app

copy requirements.txt .

RUN pip install -r requirements.txt