def explain(data):
    reasons = []

    if data["temperature"] > 35:
        reasons.append("High temperature")

    if data["rainfall"] < 2:
        reasons.append("No rainfall forecast")

    if data["soil_moisture"] < 25:
        reasons.append("Low soil moisture")

    return reasons