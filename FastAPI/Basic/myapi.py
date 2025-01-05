from fastapi import FastAPI, Path;

app=FastAPI();

students={
    1:{
        "name":"John",
        "age": 12,
        "class":"6th"
    }
}


@app.get("/")
def index():
    return {"name": "Welcome...."}


# @app.get("/get-student/{student_id}")
# def get_student(student_id:int):
#     return students[student_id]


@app.get("/get-student/{student_id}")
def get_student(student_id:int=Path(..., description="the ID of the student we want to view", gt=0, lt=3)):
    return students[student_id]







