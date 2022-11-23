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
    print(productions)
    while productions:
        print("masuk")
        rule = productions.pop()
        print(rule)
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

makeCnf('grammar_cfg.txt')
