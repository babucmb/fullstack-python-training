# post api call is used to store the data at server side

from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
# class whihc store the sturture of data
class Student(BaseModel):
    name:str
    age: int

student_data={}  # empty database
@app.post("/student/")
def create_student(s : Student):
    student_data[s.name]=s.name # Storing the name in database
    student_data[s.age]=s.age # Stroing the age in database
    return student_data[s.name],student_data[s.age] # return the stored data
