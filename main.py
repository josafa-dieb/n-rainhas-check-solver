import dpll

if __name__ == "__main__":
    #mapear os simbolos proposicionais (atomos)
    N = 5
    counter = 1

    mapping_to_int = {}
    mapping_to_int_inv = {}

    positions = [[i,j] for i in range(1,N+1) for j in range(1,N+1)]

    for position in positions:
        key = f"Q_{position[0]}_{position[1]}"
        mapping_to_int[key] = counter
        mapping_to_int_inv[counter] = key
        counter+=1

    #cada linha possui pelo menos uma rainha
    for i in range(1,N+1):
        line = []
        for j in range(1, N+1):
            line.append(mapping_to_int[f"Q_{i}_{j}"])
        dpll.add_clause(line)

    #cada coluna possui no maximo uma rainha
    for j in range(1,N+1):
        for i in range(1, N+1):
            other_indexes = list(range(1,N+1))
            other_indexes.remove(i)
            for other in other_indexes:
                #Q_i_j -> ~Q_k_j v ~Q_k_j2 === ~Q_i_j v ~Q_k_j v ~Q_k_j2
                clause = [-mapping_to_int[f"Q_{i}_{j}"], -mapping_to_int[f"Q_{other}_{j}"]]
                dpll.add_clause(clause)

    # Diagonal principal
    [dpll.add_clause([-mapping_to_int[f"Q_{i}_{j}"]]) for i in range(1, N+1) for j in range(1, N+1) if i-j == -1]

    # Diagonal secundaria
    [dpll.add_clause([-mapping_to_int[f"Q_{i}_{((N+2)-i-1)}"]]) for i in range(1, N+1) ]

    [print("Existe um valor satisfazivel") if dpll.solver() else print("não existe um valor satisfazivel")]

    for i in dpll.get_model():
        print(mapping_to_int_inv[i])
    print(mapping_to_int_inv)