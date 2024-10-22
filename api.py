from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()




employee = {
    1790: {
        "name": "a",
        "designation": "Software Engineer"
    },

    1791: {
        
        "name": "Md. Rashed Mizan",
        "designation": "Software Engineer"

    }
}

class Employee(BaseModel):
    name: str
    designation: str

class UpdateEmployee(BaseModel):
    name: Optional[str]=None
    designation: Optional[str]=None


@app.get("/home")
def home():
    return {"message":"Hello from FastAPI"}


@app.get("/get-employee/{pin}")
def get_employee(pin:int = Path(description="employee PIN")):
    return employee[pin]


@app.get("/get-employee-by-name")
def get_employee(name:Optional[str]=None):
    for _,details in employee.items():
        if details["name"] == name:
            return details
    return {"message": "Data not found!"}


@app.get("/get-employee-by-name-v2/{pin}")
def get_employee(pin:int, name:Optional[str]=None):
    for _,details in employee.items():
        if details["name"] == name:
            return details
    
    return employee[pin]
    

@app.post("/create-employee/{employee_id}")
def create_employee(employee_id: int, new_employee_data: Employee):
    if employee_id in employee:
        return {"message": "Employee already exists"}
    employee[id] = new_employee_data
    return new_employee_data


@app.put("/update-employee/{employee_id}")
def update_employee(employee_id: int, updated_employee_data: UpdateEmployee):
    if employee_id not in employee.keys():
        return {"message": "Employee doesn't exist!"}
    
    if updated_employee_data.name != None:
        employee[employee_id]["name"] = updated_employee_data.name
    if updated_employee_data.designation != None:
        employee[employee_id]["designation"] = updated_employee_data.designation
    return employee[employee_id]


@app.delete("/delete-employee/{employee_id}")
def delete_employee(employee_id:int):
    if employee_id not in employee.keys():
        return {"message": "Employee doesn't exist!"}
    del employee[employee_id]
    return {"message": f"Employee with id {employee_id} deleted successfully"}