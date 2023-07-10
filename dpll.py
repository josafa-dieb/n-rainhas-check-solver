from simplify import simplify
from copy import deepcopy

__dpll_cnf = []
__sat = []
def _literal(cnf):
    clauses = cnf
    literal = None
    for clause in clauses:
        for L in clause:
            if -L in clause:
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

    L  = _literal(dpll_cnf)
    
    if DPLL(dpll_cnf + [[L]]):
        return True
    elif DPLL(dpll_cnf + [[-L]]):
        return True
    else:
        return False


def add_clause(clause:list):
    __dpll_cnf.append(clause)
    
def get_model():
    return __sat

def solver():
    return DPLL(__dpll_cnf)


if __name__ == "__main__":
    print("""
          Esse arquivo deve ser utilizado de forma modular:
          import DPLL
          
          Será importado as seguintes funções:
          + add_clause    - para adicionar as clausulas de uma cnf
          + dpll          - implementação do algoritimo dpll
          + solver        - retorna a satisfiabilidade das clausas adicionadas
          
          """)