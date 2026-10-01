# Path parameter
# inside the URL path itself you can pass the value


from fastapi import FastAPI
app=FastAPI()

@app.get("/Product/{product_id}")   #--> this is the path parameter value
def product_details(product_id: int):
    return {f"Product ID is {product_id}"}

