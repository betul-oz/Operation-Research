#this question taken from operations research book by Wayne L. Winston in page 362

from pulp import *

prob = LpProblem("Transshipment", LpMinimize)

plants = ["Plant1", "Plant2", "Plant3"]
city = ["City1", "City2", "City3", "City4"]

supply = {"Plant1": 35,
          "Plant2": 50,
          "Plant3": 40}

demand = {"City1": 45,
          "City2": 20,
          "City3": 30,
          "City4": 30}

cost_matrix = [[0, 10, 25, 0],
               [45, 0, 5, 0],
               [0, 10, 0, 30]]

routes = [(p, c) for p in plants for c in city]

amount_vars = LpVariable.dicts("Route", (plants, city), 0, None, LpInteger)

cost = {(p, c): cost_matrix[plants.index(p)][city.index(c)] for p in plants for c in city}

prob += lpSum(amount_vars[p][c] * cost[p, c] for (p, c) in routes)

for p in plants:
    prob += lpSum(amount_vars[p][c] for c in city) <= supply[p]

for c in city:
    prob += lpSum(amount_vars[p][c] for p in plants) >= demand[c]

prob.solve()

for v in prob.variables():
    if v.varValue > 0:
        print(v.name, "=", v.varValue)