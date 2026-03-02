from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
import joblib

data = pd.read_csv("ml/train_data.csv")

X = data[["rainfall_trend","temperature_trend","soil_dryness"]]
y = data["risk"]

model = GradientBoostingClassifier()
model.fit(X, y)

joblib.dump(model, "ml_models/risk_model.pkl")