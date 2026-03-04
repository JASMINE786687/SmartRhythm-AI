def dam_status(storage_percent):
    if storage_percent > 60:
        return "Safe"
    elif storage_percent > 30:
        return "Warning"
    else:
        return "Critical"