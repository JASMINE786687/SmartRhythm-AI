import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = pd.read_csv("train_data.csv")

X = data[["soil_moisture","temperature","area"]]
y = data["water_quantity"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "quantity_model.pkl")
print("Water Quantity Model Saved")