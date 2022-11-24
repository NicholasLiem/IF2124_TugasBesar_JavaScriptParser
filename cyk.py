def dictionary_CNF(CNF):
    new_dict = {}
    for rules in CNF :
        new_dict[str(rules[0])] = []

    for rules in CNF:
        productions = []
        for i in range(1,len(rules)):
            temp = rules[i]
            productions.append(temp)
        new_dict[str(rules[0])].append(productions)
    return new_dict

def CYK_parse(CNF, arrayInput):
    N = len(arrayInput)
    CNF = dictionary_CNF(CNF)
    T = [[set([]) for j in range(N)] for i in range(N)]

    for j in range(N):
        for head, body in CNF.items():
            for rule in body:
                if len(rule) == 1 and rule[0] == "'" +arrayInput[j] + "'":
                    T[j][j].add(head)
        for i in range(j, -1, -1):
            for k in range(i, j):
                for head, body in CNF.items():
                    for rule in body:
                        if len(rule) == 2 and rule[0] in T[i][k] and rule[1] in T[k + 1][j]:
                            T[i][j].add(head)
    return len(T[0][N - 1]) != 0