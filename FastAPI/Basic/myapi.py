from fastapi import FastAPI, Path;
from typing import Optional;
from pydantic import BaseModel;

app=FastAPI();

students={
    1:{
        "name":"John",
        "age": 12,
        "year":"Year 6th"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str
 
 
 
class UpdateStudent(BaseModel):
     name: Optional[str]=None
     age: Optional[int]=None
     year: Optional[str]=None

@app.get("/")
def index():
    return {"name": "Welcome...."}


# @app.get("/get-student/{student_id}")
# def get_student(student_id:int):
#     return students[student_id]




# Get student details by id
@app.get("/get-student/{student_id}")
def get_student(student_id:int=Path(..., description="the ID of the student we want to view", gt=0, lt=3)):
    return students[student_id]




# Get student details by name
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id:int, name: Optional[str] = None, test:int):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"Data":"Not found"}



# Post method
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    
    print(student) 
    
    students[student_id] = student;
    return {"message": "Student created successfully", "student": student}



@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student doesn't exist"}
    
    # Update only the provided fields
    existing_student = students[student_id]
    if student.name is not None:
        existing_student["name"] = student.name
    if student.age is not None:
        existing_student["age"] = student.age
    if student.year is not None:
        existing_student["year"] = student.year
    
    # Return updated data
    return {"message": "Student updated successfully", "student": existing_student}
    



@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error":"Student not found!"}

    del students[student_id]
    return {"message":"Student deleted successfully"}









