from sklearn.linear_model import LinearRegression
import pandas as pd
import joblib
import os

# Ensure correct path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "ml", "train_data.csv")
MODEL_PATH = os.path.join(BASE_DIR, "ml_models", "quantity_model.pkl")

data = pd.read_csv(DATA_PATH)

X = data[["soil_moisture", "temperature", "area"]]
y = data["water_quantity"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, MODEL_PATH)
print("✅ Quantity model saved successfully")