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

def CYK(CNF, arrayInput):
    N = len(arrayInput)
    CNF = dictionary_CNF(CNF)
    table = [[set([]) for j in range(N)] for i in range(N)]

    for j in range(N):
        for leftRule, rightRules in CNF.items():
            for rule in rightRules:
                if len(rule) == 1 and rule[0] == "'" +arrayInput[j] + "'":
                    table[j][j].add(leftRule)
        for i in range(j, -1, -1):
            for k in range(i, j):
                for leftRule, rightRules in CNF.items():
                    for rule in rightRules:
                        if len(rule) == 2 and rule[0] in table[i][k] and rule[1] in table[k + 1][j]:
                            table[i][j].add(leftRule)
    return len(table[0][N - 1]) != 0