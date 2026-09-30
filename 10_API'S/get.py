# get API Call
# Import the required FASTAPI 
# TO RUN:- fastapi dev .\get.py
# FASTAPI is standing between server and client

from fastapi import FastAPI

# Create object for using FastAPI()
app=FastAPI()

@app.get("/")
def dashboard():
    return "Welcom to dashboard"


@app.get("/Home")
def Home():
    return "Welcome to Home page"

@app.get("/student/marks")
def Home():
    return "81,22,34,54,67,89,76"

