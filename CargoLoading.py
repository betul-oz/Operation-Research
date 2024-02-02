from pulp import *

model = LpProblem("CargoLoading", LpMaximize)

x1 = LpVariable("x1", 0, None, LpInteger)
x2 = LpVariable("x2", 0, None, LpInteger)
x3 = LpVariable("x3", 0, None, LpInteger)

#objective function
model += 12 * x1 + 25 * x2 + 38 * x3

#Constraints
model += x1 + 2 * x2 + 3 * x3 <= 10

model.solve()

for v in model.variables():
    print(v.name, "=", v.varValue)

# The status of the solution is printed to the screen
print("Status:", LpStatus[model.status])