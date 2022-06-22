"""Main module. Entrypoint for the app"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Basic route"""
    return {"message": "Hello World"}
