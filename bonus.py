from rules import createToken
import sys

operator_arit = ["ADD","SUB","MUL","DIV","MOD","POW","XOR","BITLEFT","BITRIGHT","BITOR","BITAND","BITNOT"]
operator_assign = ["EQ","ADDAS","SUBAS","MULAS","DIVAS","MODAS","POWAS","BITORDAS","BITANDAS","NULLISHAS"]
operator_logic = ["L","G","GEQ","LEQ","STRICTNEQ","NEQ","STRICTEQ","ISEQ","AND","OR"]
value=["NUM","STRING","BOOL","LIST"]
tanda_kurung = ["KBKI","KBKA","KKKI","KKKA","KSKI","KSKA"]
#belum bisa handle list dan object 

def cekToken(token):
    token = [value for value in token if value != "NEWLINE"]
    index= 0
    while index < len(token):
        if(token[index] == "FUNCTION"):
            function_content = []
            count = 1
            if_content =[]
            while(count%2 != 0 and index < len(token)):
                if(token[index] == "KKKA"):
                    if(count != 1):
                        count += 1
                function_content.append(token[index])
                index += 1
        elif(token[index] == "IF"):
            if_content = []
            count = 1
            while(count%2 != 0 and index < len(token)):
                if(token[index] == "KKKA"):
                    count += 1
                if_content.append(token[index])
                index += 1
            if("BREAK" in if_content):
                print("ERROR : SYNTAX BREAK, IF CAN'T USE BREAK")
                sys.exit(1)
            if("RETURN" in if_content):
                print("ERROR :SYNTAX RETURN, IF CAN'T RETURN ANY VALUE")
                sys.exit(1)
                break
        elif(token[index] == "WHILE"):
            while_content =[]
            count = 1
            while(count%2 != 0 and index < len(token)):
                if(token[index] == "KKKA"):
                    count += 1
                while_content.append(token[index])
                index += 1
            if("RETURN" in while_content):
                print("ERROR : SYNTAX RETURN, WHILE CAN'T RETURN ANY VALUE")
                sys.exit(1)
                break
        elif(token[index] == "ELSE"):
            print("ERROR : SYNTAX ELSE, EXPECTED IF STATEMENT BEFORE")
            sys.exit(1)
            break
        elif(token[index] == "ELSE_IF"):
            print("ERROR : SYNTAX ELSE IF, EXPECTED IF STATEMENT BEFORE ")
            sys.exit(1)
            break
        elif(token[index] == "SWITCH"):
            switch_content =[]
            count = 1
            while(count%2 != 0 and index < len(token)):
                if(token[index] == "KKKA"):
                    count += 1
                switch_content.append(token[index])
                index += 1
            if("RETURN" in switch_content):
                print("ERROR : SYNTAX RETURN, SWITCH CAN'T RETURN ANY VALUE ")
                sys.exit(1)
        elif(token[index] == "TYPE"):
            if( index+1 < len(token) and token[index + 1] == "ID"):
                if(index + 2 < len(token)):
                    if not (token[index + 2] == "EQ"):   
                        print("ERROR : SYNTAX ASSIGN VARIABEL HARUS MENGGUNAKAN '='")
                        sys.exit(1)
        elif(token[index] == "CASE"):
            print("ERROR : SYNTAX CASE HARUS BERADA DALAM SWITCH BLOCK")
            sys.exit(1)
        elif(token[index] == "DEFAULT"):
            print("ERROR : SYNTAX DEFAULT HARUS BERADA DALAM SWITCH BLOCK")
            sys.exit(1)
        index +=1

# token = createToken("tes.js")
# cekToken(token)
