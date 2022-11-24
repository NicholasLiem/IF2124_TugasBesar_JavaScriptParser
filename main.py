from grammar_reader import read_grammar,convert_grammar
from rules import createToken
from cyk import CYK_parse

tokens = createToken('tes.js')
print(tokens)
cfg = read_grammar('grammar_cfg.txt')
# print(cfg)
cnf = convert_grammar(cfg)
# print(cnf)

if(CYK_parse(cnf,tokens)):
    print("SYNTAX TRUE")
else:
    print("SYNTAX FALSE")


