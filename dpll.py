from simplify import simplify
from copy import deepcopy

__dpll_cnf = []

def literal(cnf):
    clauses = cnf
    literal = None
    for clause in clauses:
        for L in clause:
            if -L != clause:
                literal = L
                break

        if literal != None:
            break
    return clauses[0][0] if literal == None else literal

def DPLL(cnf):
    
    dpll_cnf = deepcopy(simplify(cnf))
                        
    if dpll_cnf == []:
        return True
    elif [] in dpll_cnf:
        return False

    L  = literal(dpll_cnf)

    if DPLL(dpll_cnf + [[L]]):
        return True
    elif DPLL(dpll_cnf + [[-L]]):
        return True
    else:
        return False


def add_clause(clause:list):
    __dpll_cnf.append(clause)

def solver():
    return DPLL(__dpll_cnf)