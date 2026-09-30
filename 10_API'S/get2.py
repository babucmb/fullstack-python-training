# Query Parameters passing
# Query Parameters is sefined by "?" in the URL

from fastapi import FastAPI

app=FastAPI()

@app.get("/greet")
def display(name:str="Guest"):  #  Parameter passing
    return {f"Hello:{name}"}