import numpy as np

def equity_score(allocation_dict):
    values = list(allocation_dict.values())
    return round(np.std(values) / np.mean(values), 3)