RULE = {}

def isTerminal(string):
    terminals = ["STRING","NUM","NEWLINE","KBKI","KBKA","KSKI",
                "KSKA","KKKI","KKKA","TITIKKOMA","TITIKDUA","POWAS",
                "POW","FLOORDIVAS","FLOORDIV","MULAS","DIVAS","ADDAS",
                "SUBAS","MODAS","ARROW","ADD","SUB","MUL","DIV","MOD",
                "LEQ","L","GEQ","G","NEQ","ISEQ","EQ","AND","OR","NOT",
                "IF","ELSE","ELSE IF","FOR","IN","OF","DO","WHILE","SWITCH",
                "CASE","DEFAULT","TRY","CATCH","FINALLY","THROW","DELETE","CONTINUE",
                "BREAK","FALSE","TRUE","CLASS","FUNCTION","RETURN","FROM","IMPORT","AS",
                "RAISE","WITH","NULL","TYPE","COMMA","KARTITIK","TITIK","IS","MULTILINE","ID","NEW"]
    return string in terminals

def read_grammar(nama_file):
    files = open(nama_file)
    cfg = []
    for file in files : 
        file = file.replace('->',"")
        cfg.append(file.split())
    return cfg

def addRule(rule):
    global RULE
    if(rule[0] not in RULE):
        RULE[rule[0]] = []
    RULE[rule[0]].append(rule[1:])

def add_rule(rule):
    # Menambah aturan ke kamus
    global RULE_DICT

    if rule[0] not in RULE_DICT:
        RULE_DICT[rule[0]] = []
    RULE_DICT[rule[0]].append(rule[1:])

def convert_grammar(grammar):
    # Meng-convert cfg menjadi cnf
    global RULE

    unit_prod, result = [], []
    idx = 0

    for rule in grammar:
        new_rules = []
        if len(rule) == 2 and rule[1][0] != "'":
            unit_prod.append(rule)
            add_rule(rule)
            continue
        elif len(rule) > 2:
            terminals = [(item, i) for i, item in enumerate(rule) if item[0] == "'"]
            if isTerminal(rule[0]):
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

    while unit_prod:
        rule = unit_prod.pop()
        if rule[1] in RULE:
            for item in RULE[rule[1]]:
                new_rule = [rule[0]] + item
                print(new_rule)
                if len(new_rule) > 2 or new_rule[1][0] == "'":
                    result.insert(0,new_rule)
                else:
                    unit_prod.append(new_rule)
                add_rule(new_rule)
    return result

cfg = read_grammar('grammar_cfg.txt')
print(convert_grammar(cfg))
