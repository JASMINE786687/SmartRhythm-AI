import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("ml/train_data.csv")

X = data[["temperature","humidity","rainfall","soil_moisture","crop_stage"]]
y = data["irrigation_required"]

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

joblib.dump(model, "ml_models/irrigation_model.pkl")
print("Irrigation model saved")