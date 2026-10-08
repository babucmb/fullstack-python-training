# Posting the request using pydantic
# post api call is used to store the data at server side
from fastapi import FastAPI

from pydantic import BaseModel

class student(BaseModel):
    name:str
    age: int
app=FastAPI()

@app.post("/students")
def store_data(student:student):
    return {f"Hello {student.name} your age is {student.age}"}

