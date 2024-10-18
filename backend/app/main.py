# This is a simple way to create tables on startup
# backend/app/main.py
from fastapi import FastAPI
from app.database import engine, Base

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Include your routes
