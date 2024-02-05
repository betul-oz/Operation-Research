from pulp import *

model = LpProblem("Diet Problem", LpMinimize)

x1 = LpVariable("ChickenPercent", 0, None, LpContinuous)
x2 = LpVariable("BeefPercent", 0, None, LpContinuous)
x3 = LpVariable("MuttonPercent", 0, None, LpContinuous)

model += 0.03*x1 + 0.05*x2 + 0.02*x3, "Total Cost of Ingredients per can"

model += 4*x1 + 2*x2 + 2*x3 >= 27, "ProteinRequirement"
model += 420*x1 + 25*x2 + 21*x3 >= 240, "CarbohydrateRequirement"
model += 90*x1 + 110*x2 + 100*x3 >= 27, "calorieRequirement"
model += x1 + x2 + x3 >= 12, "Box size"

model.solve()

for v in model.variables():
    print(v.name, "=", v.varValue)

print("Total Cost of Ingredients per can = ", value(model.objective))