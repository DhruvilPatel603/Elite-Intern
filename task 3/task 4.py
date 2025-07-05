

from pulp import *

prob = LpProblem("Maximize_Profit", LpMaximize)

x = LpVariable("Product_A", lowBound=0)
y = LpVariable("Product_B", lowBound=0)

prob += 20*x + 30*y, "Total Profit"
prob += 2*x + 4*y <= 100
prob += 3*x + y <= 90

prob.solve()

print(f"Status: {LpStatus[prob.status]}")
print(f"Produce {x.varValue} units of Product A")
print(f"Produce {y.varValue} units of Product B")
print(f"Maximum Profit: ₹{value(prob.objective)}")
