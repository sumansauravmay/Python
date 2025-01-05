from fastapi import FastAPI;

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


@app.get("/get-student/{student_id}")
def get_student(student_id:int):
    return students[student_id]







