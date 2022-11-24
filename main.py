from grammar_reader import *
from rules import createToken
from cyk import CYK_parse

def displayResult(string):
    print("=================================")
    print("    RESULT : SYNTAX "+string)
    print("=================================")

print("TOKENIZING...")
tokens = createToken('tes.js')
print(tokens)
print("TOKENIZING - DONE")

print("READING CFG GRAMMAR...")
cfg = read_grammar('grammar_cfg.txt')
# print(cfg)
print("READING CFG GRAMMAR - DONE")

print("CONVERTING CFG TO CNF...")
cnf = convert_grammar(cfg)
# write_cnf(cnf, "cnf.txt")
print("CONVERTING CFG TO CNF - DONE")


print("CHECKING TO CYK...")
if(CYK_parse(cnf,tokens)):
    print("CHECKING TO CYK - DONE")
    displayResult("TRUE")
else:
    print("CHECKING TO CYK - DONE")
    displayResult("FALSE")


