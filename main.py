from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name":"Usman",
        "age":23,
        "title":"ML Engineer"
    }
}

class Student(BaseModel):
    name: str
    age: int
    title: str
    

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    title: Optional[str] = None
    


@app.get("/")
def index():
    return {"Name":"Usman Malik",
            "Title":"Junior ML Engineer"}
# PATH PARAMETERS

@app.get("/get-student/{student_id}")
def get_student(student_id: int=Path(None,description="The ID of the student you want to view",gt=0, lt=3)):
    return students[student_id]

# QUERY PARAMETERS

@app.get("/get-by-name/{name}")
def get_student_by_name(name: Optional [str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data":"Not Found"}


# POST REQUEST METHOD


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error":"Student already exists"}
    
    students[student_id] = student
    return students[student_id]

# PUT METHOD

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error":"Student doesn't exists"}

    if student.name != None:
        students[student_id].name = student.name
        
    if student.age != None:
        students[student_id].age = student.age
    
    if student.title != None:
        students[student_id].title = student.title
        
    return students[student_id]


# DELETE METHOD

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error":"Student doesn't exists"}
    
    del students[student_id]
    return {"Message": "Student {student_id} Deleted Successfully"}
    
    


