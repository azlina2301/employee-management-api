import os
import psycopg 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    name: str
    department: str
    salary: float

@app.get("/")
def home():
    return {"message": "Welcome to the Employee Management System!"}

@app.get("/employees")
def get_employees():

    conn = psycopg.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM employees ORDER BY id;")

        rows = cur.fetchall()
    conn.close()

    employees = []
    for row in rows:
        employee = {
            "id": row[0],
            "name": row[1],
            "department": row[2],
            "salary": float(row[3])
        }
        employees.append(employee)
    return employees

@app.post("/employees")
def create_employee(employee: Employee):
    conn = psycopg.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    with conn.cursor() as curr:

        curr.execute(
            """
            INSERT INTO employees(name, department, salary)
            VALUES(%s, %s, %s)
            RETURNING id
            """,
            (employee.name, employee.department, employee.salary)
        )

        employee_id = curr.fetchone()[0]
        conn.commit()
    conn.close()

    return {
        "message": "Employee created successfully",
        "id": employee_id
    }


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    conn = psycopg.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM employees where id = %s",
            (employee_id,)
        )

        row = cur.fetchone()

        conn.close()

        if row is None:
            raise HTTPException(
                status_code=404,
                detail="Employee not found"
            )

        return {
            "id": row[0],
            "name": row[1],
            "department": row[2],
            "salary": float(row[3])
        }