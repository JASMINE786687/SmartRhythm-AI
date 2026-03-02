from fastapi import FastAPI
from backend.ml_service import irrigation_model

app = FastAPI(title="SmartRhythm-AI Backend")

@app.get("/")
def root():
    return {"message": "SmartRhythm-AI Backend is running"}

@app.post("/predict-irrigation")
def predict_irrigation(data: dict):
    features = [[
        data["temperature"],
        data["humidity"],
        data["rainfall"],
        data["soil_moisture"],
        data["crop_stage"]
    ]]
    result = irrigation_model.predict(features)
    return {"irrigation_required": bool(result[0])}