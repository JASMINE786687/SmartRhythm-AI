import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

irrigation_model = joblib.load(
    os.path.join(BASE_DIR, "ml_models", "irrigation_model.pkl")
)