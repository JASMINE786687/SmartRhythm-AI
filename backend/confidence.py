def calculate_confidence(missing_ratio, accuracy, freshness_days):
    freshness_weight = max(0.5, 1 - freshness_days/7)
    confidence = (1 - missing_ratio) * accuracy * freshness_weight
    return round(confidence * 100, 2)