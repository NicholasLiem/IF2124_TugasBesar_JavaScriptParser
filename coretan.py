import rules

RULE = {} # Kamus untuk menyimpan cnf

def write_cnf(fileCNF,namafile):
    # Menulis hasil convert ke dalam file txt
    file = open(namafile, 'w')
    for cnf in fileCNF:
        file.write(cnf[0])
        file.write(" -> ")
        for i in cnf[1:]:
            file.write(i)
            file.write(" ")
        file.write("\n")
    file.close()


def read_grammar(filename):
    # Baca cfg dari file
    with open(filename) as cfg:
        lines = cfg.readlines()
    return [x.replace("->", "").split() for x in lines]

def add_rule(rule):
    # Menambah aturan ke kamus
    global RULE

    if rule[0] not in RULE:
        RULE[rule[0]] = []
    RULE[rule[0]].append(rule[1:])

def convert_grammar(grammar):
    # Meng-convert cfg menjadi cnf
    global RULE

    productions, result = [], []
    idx = 0

    for rule in grammar:
        new_rules = []
        if len(rule) == 2 and rule[1][0] != "'":
            productions.append(rule)
            add_rule(rule)
            continue
        elif len(rule) > 2:
            terminals = [(item, i) for i, item in enumerate(rule) if item[0] == "'"]
            if terminals:
                for item in terminals:
                    rule[item[1]] = f"{rule[0]}{str(idx)}"
                    new_rules += [f"{rule[0]}{str(idx)}", item[0]]
                idx += 1
            while len(rule) > 3:
                new_rules.append([f"{rule[0]}{str(idx)}", rule[1], rule[2]])
                rule = [rule[0]] + [f"{rule[0]}{str(idx)}"] + rule[3:]
                idx += 1
        add_rule(rule)
        result.append(rule)
        if new_rules:
            result.extend(new_rules)
    while productions:
        rule = productions.pop()
        if rule[1] in RULE:
            for item in RULE[rule[1]]:
                new_rule = [rule[0]] + item
                # print(new_rule)
                if len(new_rule) > 2 or new_rule[1][0] == "'":
                    result.insert(0,new_rule)
                else:
                    productions.append(new_rule)
                add_rule(new_rule)
    return result

def makeCnf(filename):
    cfg = read_grammar(filename)
    cnf = convert_grammar(cfg)
    write_cnf(cnf, "cnf.txt")
        
def toDict(grammar):
    ans = {}
    for g in grammar:
        ans[str(g[0])] = []

    for g in grammar:
        prod = []
        for i in range(1,len(g)):
            temp = g[i]
            prod.append(temp)
        ans[str(g[0])].append(prod)
    return ans

def CYK_parse(CNF, arrayInput):
    N = len(arrayInput)
    CNF = toDict(CNF)
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

tokens = rules.createToken("tes.js")
print(tokens)
cfg = read_grammar("grammar_cfg.txt")
print("D0ne reading")
cnf = convert_grammar(cfg)
print("CNF DONE")

if(CYK_parse(cnf,tokens)):
    print("Bener")
else:
    print("Salah")



