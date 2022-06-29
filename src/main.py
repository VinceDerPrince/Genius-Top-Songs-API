from fastapi import FastAPI
import scraper as _scraper

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"welcome to the Top 10 Songs on Genius"}

@app.get("/charts")
async def current_charts():
    return _scraper.charts_of_the_day()

@app.get("/specific")
async def specific_chart(num: int):
    return _scraper.specific_chart(num)
