from fastapi import FastAPI
from scraper import scraper

app = FastAPI()

@app.get("/")

async def read_item():
    return scraper() 
