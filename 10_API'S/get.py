# get API Call
# Import the required FASTAPI 
# TO RUN:- fastapi dev .\get.py

from fastapi import FastAPI

# Create object for using FastAPI()
app=FastAPI()

@app.get("/")
def dashboard():
    return "Welcom to dashboard"


