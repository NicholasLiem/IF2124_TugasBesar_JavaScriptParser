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


def read_grammar(cfgfilepath):
    # Baca cfg dari file yang berisi grammar cfg
    cfg = open(cfgfilepath)
    lines = cfg.readlines()
    for i in range (len(lines)):
        # menghilangkan arrow
        lines[i] = lines[i].replace("->", "")
        # memisahkan isi string dengan spasi sebagai pemisah
        # state awal selalu menjadi index pertama (index 0)
        lines[i] = lines[i].split()
    # dikembalikan sebagai sebuah list besar yang berisi list-list
    return lines

def add_rule(rule):
    # Menambah aturan ke kamus 
    global RULE

    # melakukan cek apakah sebuah rule[0] (head) sudah ada di list
    if rule[0] not in RULE:
        # jika belum ada, maka rule[0] (head) ditambahkan sebagai dictionary baru yang memiliki value list kosong
        RULE[rule[0]] = []
    # menambahkan rule[1:] (sisi kanan transisi) sebagai sebuah list dan ditambahkan ke dalam list yang memiliki key = rule[0]
    RULE[rule[0]].append(rule[1:])

def convert_grammar(cfg_grammar):
    # Meng-convert cfg menjadi cnf
    global RULE

    productions, result = [], []
    idx = 0

    for rule in cfg_grammar:
        new_rules = []
        if len(rule) == 2 and rule[1][0] != "'":
            # untuk transisi satu-satu (a -> b) dan a bukan terminal
            productions.append(rule)
            add_rule(rule)
            continue
        elif len(rule) > 2:
            # untuk transisi yang menghasilkan lebih dari satu hasil (sisi kanan)
            terminals = []
            for i, item in enumerate(rule):
                if (item[0] == "'"):
                    terminals.append(([item,i]))
            # terminals = [(item, i) for i, item in enumerate(rule) if item[0] == "'"]
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


def makeCnf(filepath):
    # membaca filepath tertentu yang mengandung grammar cfg
    cfg = read_grammar(filepath)
    # mengubah cfg menjadi cnf
    cnf = convert_grammar(cfg)
    # menuliskan hasil cnf ke txt
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
write_cnf(cnf,'cnf.txt')
if(CYK_parse(cnf,tokens)):
    print("Bener")
else:
    print("Salah")
