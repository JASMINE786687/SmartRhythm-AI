def estimate_arrival(distance_km, flow_speed_kmph):
    hours = distance_km / flow_speed_kmph
    return round(hours, 2)