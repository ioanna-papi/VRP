from VRP_Model import *
from Solver import *

#1st question
m1 = Model()
m1.BuildModel()

#3rd question
print()
print("Solution with Nearest Neighbor Method:")
print()
s1 = Solver(m1)
sol = s1.solve()
print()

#2nd question
dist = s1.CalculateDistance(s1.sol)
print("Total distance with Nearest Neighbor Method: ", dist)
print()
print()

#4th question
print("Solution after Local Search:")
print()
loops = s1.LocalSearch()
s1.ReportSolution(s1.sol)
dist = s1.CalculateDistance(s1.sol)
print()
print("Total distance after Local Search: ", dist)
print("Total routes after Local Search: ", len(s1.sol.routes))
print ("Termination after ", loops, " loops.")
print()
print()

#5th question
print("Solution with VND Algorithm:")
print()
s1.VND()
s1.ReportSolution(s1.sol)
dist = s1.CalculateDistance(s1.sol)
print()
print("Total distance with VND Algorithm: ", dist)
print()
