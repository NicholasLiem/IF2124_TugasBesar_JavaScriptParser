def isTerminal(string):
    terminals = ["STRING","NUM","NEWLINE","KBKI","KBKA","KSKI",
                "KSKA","KKKI","KKKA","TITIKKOMA","TITIKDUA","POWAS",
                "POW","FLOORDIVAS","FLOORDIV","MULAS","DIVAS","ADDAS",
                "SUBAS","MODAS","ARROW","ADD","SUB","MUL","DIV","MOD",
                "LEQ","L","GEQ","G","NEQ","ISEQ","EQ","AND","OR","NOT",
                "IF","ELSE","ELSE IF","FOR","IN","OF","DO","WHILE","SWITCH",
                "CASE","DEFAULT","TRY","CATCH","FINALLY","THROW","DELETE","CONTINUE",
                "BREAK","FALSE","TRUE","CLASS","FUNCTION","RETURN","FROM","IMPORT","AS",
                "RAISE","WITH","NULL","TYPE","COMMA","KARTITIK","TITIK","IS","MULTILINE","ID"]

def read_grammar(nama_file):
    files = open(nama_file)
    cfg = []
    for file in files : 
        file = file.replace('->',"")
        cfg.append(file.split())
    return cfg

def convert_grammar(cfg):
    print("gatau susah")

