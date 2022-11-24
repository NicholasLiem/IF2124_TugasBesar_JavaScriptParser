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
    # print(productions)
    while productions:
        # print("masuk")
        rule = productions.pop()
        # print(rule)
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

makeCnf('grammar_cfg.txt')