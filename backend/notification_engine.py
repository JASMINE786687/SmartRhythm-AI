def generate_notification(prediction):
    messages = []

    if prediction["irrigation"] == "YES":
        messages.append("Irrigation recommended today.")

    if prediction["risk"] == "High":
        messages.append("High drought risk detected.")

    if prediction["confidence"] < 70:
        messages.append("Low confidence advisory. Monitor manually.")

    return messages