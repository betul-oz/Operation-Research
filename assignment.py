#this problem taken from operation reasearch book in page 393


from pulp import *

lp = LpProblem("Job Assignment Problem", LpMinimize)

# Define the model
Machine = ["M1", "M2", "M3", "M4"]

job = ["J1", "J2", "J3", "J4"]

#cost matrix
cost = [
        #jobs
        #J1 J2 J3 J4
        [14, 5, 8, 7], #machine1
        [2, 12, 6, 5], #machine2
        [7, 8, 3, 9],  #machine3 
        [2, 4, 6, 10]] #machine4

# Define the problem variables
prob = LpProblem("Job Assignment Problem", LpMinimize)

# A dictionary called 'Vars' is created to contain the referenced variables (the routes)
vars = LpVariable.dicts("Route", (Machine, job), 0, None, LpInteger)

# The cost data is made into a dictionary
cost = {(m, j): cost[Machine.index(m)][job.index(j)] for m in Machine for j in job} 

# Creates a list of tuples containing all the possible routes for transport
assign = [(m, j) for m in Machine for j in job]

prob += lpSum(cost[m, j] * vars[m][j] for m, j in assign), "Total Cost"

for m in Machine:
    prob += lpSum([vars[m][j] for j in job]) == 1, \
    "Sum of Jobs out of Machine %s" % m

for j in job:
    prob += lpSum([vars[m][j] for m in Machine]) == 1, \
    "Sum of Machines into Jobs %s" % j

prob.solve()

for v in prob.variables():
    print(v.name, "=", v.varValue)

print("Status:", LpStatus[prob.status])