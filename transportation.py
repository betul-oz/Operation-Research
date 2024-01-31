# Import PuLP modeler functions
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, LpInteger

# Supply nodes
plant = ["Plant1", "Plant2", "Plant3"]

# Demand nodes
city = ["City1", "City2", "City3", "City4"]

# The number of units of supply for each supply node
supply = {"Plant1": 35,
          "Plant2": 50,
          "Plant3": 40}

# The number of units of demand for each demand node
demand = {"City1": 45,
          "City2": 20,
          "City3": 30,
          "City4": 30}

# Costs of each transportation path
cost_matrix =  [
    [8, 6, 10, 9],  # Plant1 to Cities
    [9, 12, 13, 7],  # Plant2 to Cities
    [14, 9, 16, 5]   # Plant3 to Cities
]

prob = LpProblem("Transportation Problem", LpMinimize)

# A dictionary called 'Vars' is created to contain the referenced variables (the routes)
vars = LpVariable.dicts("Route", (plant, city), 0, None, LpInteger)

for p in plant:
  prob += lpSum([vars[p][c] for c in city]) <= supply[p], \
  "Sum of Products out of Plant %s" % p

for c in city:
    prob += lpSum([vars[p][c] for p in plant]) >= demand[c], \
  "Sum of Products into Cities %s" % c

# Define the transportation costs directly
cost = {(p, c): cost_matrix[plant.index(p)][city.index(c)] for p in plant for c in city}

# Creates a list of tuples containing all the possible routes for transport
Routes = [(p, c) for p in plant for c in city]

# Define the objective function
prob += lpSum(cost[p, c] * vars[p][c] for p, c in Routes), "Total Cost"

prob.solve()

for v in prob.variables():
    print(v.name, "=", v.varValue)

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])
