# Employee Management API

A simple employee management system built with Python, FastAPI, PostgreSQL, and Docker.

## Features

- Get all employees
- Get all employees by ID
- Create new employee
- Handle employee not found errors


## Tech Stack

- Python
- FastAPI
- PostgresSQL
- psycopg
- Docker
- Docker compose

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | '/' | API Home |
| GET | '/employees' | Get all employees |
| GET | '/employees/{employee_id}' | Get employee by ID |
| POST | '/employees' | Create new employee |


## Run the application

Build and Start the container

```bash
docker compose up -d --build
```
