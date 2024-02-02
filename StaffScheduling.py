from pulp import *

model = LpProblem("StaffScheduling", LpMinimize)

# Define the shifts list
shifts = list(range(5))

#decision variables
x = LpVariable.dicts("full time employers", (shifts), 0, None, LpInteger)
y = LpVariable.dicts("part time employers", (shifts), 0, None, LpInteger)

#objective function
model += 150 * (lpSum([x[i] for i in shifts])) + 45 * (lpSum([y[i] for i in shifts]))

#Constraints For Employee starting the shift
model += x[1] + y[1] >= 6
model += x[1] + x[2] + y[2] >= 8
model += x[2] + x[3] + y[3] >= 11
model += x[3] + x[4] + y[4] >= 6 

#Constraints At least full-time employee during any shift
model += x[1] >= 1
model += x[2] >= 1
model += x[3] >= 1


model.solve()

for v in model.variables():
    print(v.name, "=", v.varValue)

# The status of the solution is printed to the screen
print("Status:", LpStatus[model.status])
