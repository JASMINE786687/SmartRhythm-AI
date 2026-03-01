from fastapi import FastAPI
from pydantic import BaseModel

# CREATE FASTAPI APP (THIS WAS MISSING)
app = FastAPI(title="SmartRhythm-AI Backend")

# Test route
@app.get("/")
def root():
    return {"message": "SmartRhythm-AI Backend is running"}