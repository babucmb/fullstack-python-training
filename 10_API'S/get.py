# get API Call


from fastapi import FastAPI

# Create object for using FastAPI()
app=FastAPI()

@app.get("/")
def dashboard():
    return "Welcom to dashboard"


