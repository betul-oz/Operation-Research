#Question taken from chapter 7 of operation and research book

# Import PuLP modeler functions
from pulp import *

#supply nodes
plant = ["Plant1", "Plant2", "Plant3"]

#demand nodes
city = ["City1", "City2", "City3", "City4"]

#the number of units of supply for each supply nod
supply = {"Plant1": 35,
          "Plant2": 50,
          "Plant3": 40}

#the number of units of demand for each demand node
demand = {"City1": 45,
          "City2": 20,
          "City3": 30,
          "City4": 30,}

#costs of each transportation path
cost_matrix =  [
    #cities
    #City1 City2 City3 City4
    [8, 6, 10, 9],#Plant1   Plants
    [9, 12, 13, 7],#Plant2
    [14, 9, 16, 5] #Plant3
    ]

prob = LpProblem("Transportation Problem", LpMinimize)

# A dictionary called 'Vars' is created to contain the referenced variables(the routes)
vars = LpVariable.dicts("Route",(plant,city),0,None,LpInteger)

for p in plant:
    prob += lpSum([vars[p][c] for c in city]) <= supply[p], "Sum of Products out of Plant %s"%p

for c in city:
    prob += lpSum([vars[p][c] for p in plant]) >= demand[c], "Sum of Products into Cities %s"%c

cost = makeDict([plant, city], cost_matrix, 0)

# Creates a list of tuples containing all the possible routes for transport
Routes = [(p,c) for p in plant for c in city]

prob.solve()

for v in prob.variables():
    print(v.name, "=", v.varValue)

# The status of the solution is printed to the screen
print("Status:", LpStatus(prob.status))
