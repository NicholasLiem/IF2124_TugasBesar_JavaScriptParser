

def read_grammar(nama_file):
    files = open(nama_file)
    cfg = []
    for file in files : 
        cfg.append(file.replace("->","").split())
    return cfg

