from copy import deepcopy

__model = []

def simplify(s_cnf):
    s_cnf = deepcopy(s_cnf)
    literal = [i for i in s_cnf if len(i) == 1] if [i for i in s_cnf if len(i) == 1] != [] else []
    count = []
    for C in literal:
        for L in C:
            if L not in count:
                count.append(L)
    i = 0
    while True:
        if i >= len(count): break
        literal = count[i]
        if literal in count and -literal not in count:
            break
        i+=1
    literal = [literal]
    
    while literal != []:
        s_cnf.remove(literal)
        if literal[0] > 0:
            __model.append(literal[0])
        cursor_i=0
        for i in range(len(s_cnf)):
            cursor_j=0
            for j in range(len(s_cnf[i-cursor_i])):
                if literal[0] == s_cnf[i-cursor_i][j-cursor_j]:
                    s_cnf.remove(s_cnf[i-cursor_i])
                    cursor_i+=1
                    break
                elif literal[0]*-1 == s_cnf[i-cursor_i][j-cursor_j]:
                    s_cnf[i-cursor_i].remove(s_cnf[i-cursor_i][j-cursor_j])
                    cursor_j+=1
                    break
        literal =  [i for i in s_cnf if len(i) == 1] if [i for i in s_cnf if len(i) == 1] != [] else []
        count = []
        for C in literal:
            for L in C:
                if L not in count:
                    count.append(L)
        i = 0
        while True:
            if i >= len(count): break
            literal = count[i]
            if literal in count and -literal not in count:
                break
            i+=1
        literal = [literal]
        if literal == [[]]: literal = []
    return s_cnf

if __name__ == "__main__":
    print("""
          Esse arquivo deve ser utilizado de forma modular:
          from simplify import simplify
          """)