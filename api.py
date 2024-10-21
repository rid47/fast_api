from fastapi import FastAPI,Path
from typing import Optional

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
    

