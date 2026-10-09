# put api call

from fastapi import FastAPI
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
    return student_data[s.name],student_data[s.age] # return the stored data

# put api call
@app.put("/student/{name}") # update the age w.r.t name of the student
def update_student(name:str, s : Student):
        student_data[s.name]=s.age
        return student_data
