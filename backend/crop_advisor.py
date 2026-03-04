def suggest_crop(risk, water_available):
    if risk == "High" and water_available < 10000:
        return "Switch to Groundnut (Low Water Crop)"
    return "Current crop suitable"