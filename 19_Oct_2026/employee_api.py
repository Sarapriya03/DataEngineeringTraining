from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Exercise 1: Create the Employee Model
class Employee(BaseModel):
    id: int
    name: str
    department: str
    designation: str
    salary: float
    city: str

employees = []

# Exercise 2: Add Employees (POST).
@app.post("/employees")
def add_employees(new_employees: list[Employee]):
    employees.extend(new_employees)
    return {
        "message": "Employees added successfully",
        "employees": new_employees
    }

# Exercise 3: Retrieve All Employees (GET)
@app.get("/employees")
def get_employees():
    return employees

# Exercise 4: Retrieve Employee by ID (GET)
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee.id == employee_id:
            return employee

    raise HTTPException(status_code=404, detail="Employee not found")

# Exercise 5: Update Employee (PUT)
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: Employee):
    for index, employee in enumerate(employees):
        if employee.id == employee_id:
            employees[index] = updated_employee
            return updated_employee

    raise HTTPException(status_code=404, detail="Employee not found")

# Exercise 6: Delete Employee (DELETE)
@app.delete("/employees/{employee_id}")
def update_employee(employee_id: int):
    for index, employee in enumerate(employees):
        if employee.id == employee_id:
            deleted = employees.pop(index)
            return {
                "message": "Employee deleted",
                "employee": deleted
            }

    raise HTTPException(status_code=404, detail="Employee not found")




