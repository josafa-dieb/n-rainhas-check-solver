import dpll


cnf = [[1, 2, -3], [1, -2, 3], [1, -2, -3], [-1, 2, 3], [-1, -2, 3], [-1, 2, -3], [-1, -2, -3]]

for clause in cnf:
    dpll.add_clause(clause)

print(dpll.solver())