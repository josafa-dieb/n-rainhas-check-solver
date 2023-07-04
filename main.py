import dpll
from pysat.solvers import Glucose4

# Normalization
file=open("./templates/5-rainhas.txt", 'r')
lines=[line.replace("\n", "").replace("\r", "").split(" ") for line in file.readlines()]

for i in range(len(lines)):
    for j in range(len(lines[i])):
        lines[i][j] = int(lines[i][j])
        if i >= 1:
            if lines[i][j] < 0:
                print("Q", end=" ")
            else:
                print("#", end=" ")
    print("")
cnf = lines[1:]
for clause in cnf:
    dpll.add_clause(clause)

print(dpll.solver())