# put api call

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()
# class whihc store the sturture of data
class Student(BaseModel):
    name:str
    age: int

student_data={}  # empty database
@app.post("/student/")
def create_student(s:Student):
    student_data[s.name]=s.age # Storing the name in database
    # student_data[s.age]=s.age # Stroing the age in database
    return {"name": s.name, "age": student_data[s.name]} # return the stored data

# put api call
@app.put("/student/{name}") # update the age w.r.t name of the student
def update_student(name:str, age:int):
    if name not in student_data:
        raise HTTPException(status_code=404, detail="This student does not exist")
    student_data[name]=age
    return student_data