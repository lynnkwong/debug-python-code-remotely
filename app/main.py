# app/main.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello(name: str | None = None):
    # Import the libary and set a breakpoint.
    # ...
    return {"Hello": name or "World!"}
