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
from backend.confidence import calculate_confidence

@app.post("/get-confidence")
def confidence_api(data: dict):
    score = calculate_confidence(
        data["missing_ratio"],
        data["accuracy"],
        data["freshness"]
    )

    msg = "Manual verification recommended" if score < 50 else "High confidence"

    return {
        "confidence": f"{score}%",
        "message": msg
    }
from backend.explanation import explain

@app.post("/get-explanation")
def explanation_api(data: dict):
    return {"reasons": explain(data)}
from optimization.allocation_engine import allocate

@app.post("/allocate-water")
def allocate_api(data: dict):
    return allocate(data["villages"], data["total_water"])