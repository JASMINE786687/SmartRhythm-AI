from pulp import *

def allocate(villages, total_water):
    prob = LpProblem("Water_Distribution", LpMinimize)

    alloc = {v: LpVariable(v, lowBound=2000) for v in villages}

    prob += lpSum(alloc.values()) <= total_water
    prob.solve()

    return {v: alloc[v].value() for v in villages}