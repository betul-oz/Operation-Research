from pulp import *

model = LpProblem("Multi-Period Production", LpMinimize)

quaters = list(range(4))
prod_cost = [3000, 3300, 3600, 3600]
inv_cost = [250, 250, 250, 250]
demand = [2300, 2000, 3100, 3000]

x = LpVariable.dicts('quater_prod_', quaters,lowBound=0, cat='Continuous')
y = LpVariable.dicts('quater_inv_', quaters,lowBound=0, cat='Continuous')

model += lpSum([prod_cost[i]*x[i] for i in quaters]) + lpSum([inv_cost[i]*y[i] for i in quaters])

for i in quaters:
    model.addConstraint(x[i]<=3000)

model.addConstraint(x[0] - y[0] == demand[0]) 

for i in quaters[1:]:
    model.addConstraint(x[i] - y[i] + y[i-1] == demand[i])

model.solve()

for v in model.variables():
    print(v.name, "=", v.varValue)

print("Total Cost of Ingredients per can = ", value(model.objective))
