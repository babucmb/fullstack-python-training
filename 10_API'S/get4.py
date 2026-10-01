# Accessing the data from databse

from fastapi import FastAPI
import asyncio

tourist_places={
    "india":["Hyd","Vizang","KPHP","Bihar"],
    "france": ["Eiffel Tower", "Louvre Museum", "French Riviera", "Mont Saint-Michel"],
    "Japan": ["Mount Fuji", "Kyoto Temples", "Tokyo Shibuya Crossing", "Osaka Castle"],
    "United States": ["Grand Canyon", "Statue of Liberty", "Yellowstone National Park", "Times Square"],
    "Italy": ["Colosseum", "Venice Canals", "Amalfi Coast", "Florence Cathedral"]
}

app=FastAPI()
@app.get("/get_places/{country}")

async def get_place(country: str):

    await asyncio.sleep(20)
    return tourist_places.get(country.lower())
