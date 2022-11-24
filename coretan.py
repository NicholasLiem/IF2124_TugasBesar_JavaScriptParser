def checkExpression(token):
    index=0
    while index <len(token):
        if token[index][1]=="ID":
            if (index+1)<len(token):
                if (token[index+1][1]=="EQ"):
                    if (index+2)<len(token):
                        if not(token[index+2][1]=="TYPE" or token[index+2][1]=="LP" or token[index+2][1]=="LAB" or token[index+2][1]=="LCB" or token[index+2][1]=="NUM" or token[index+2][1]=="STRING" or token[index+2][1]=="ID" or token[index+2][1]=="TRUE" or token[index+2][1]=="FALSE"):
                            print_error(token)
                    else:
                        print_error(token)
                elif (token[index+1][1]=="NEQ" or token[index+1][1]=="ISEQ"):
                    if (index+2)<len(token):
                        if not(token[index+2][1]=="LP" or token[index+2][1]=="LAB" or token[index+2][1]=="LCB" or token[index+2][1]=="NUM" or token[index+2][1]=="STRING" or token[index+2][1]=="ID" or token[index+2][1]=="TRUE" or token[index+2][1]=="FALSE"):
                            print_error(token)
                    else:
                        print_error(token)

                elif (token[index+1][1]=="SUB" or token[index+1][1]=="MUL" or token[index+1][1]=="POWER" or token[index+1][1]=="DIV" or token[index+1][1]=="DIVEQ" or token[index+1][1]=="MULEQ" or token[index+1][1]=="ADDEQ" or token[index+1][1]=="LESS" or token[index+1][1]=="LEQ" or token[index+1][1]=="GREATER"  or token[index+1][1]=="GEQ"):
                    if (index+2)<len(token):
                        if not(token[index+2][1]=="LP" or token[index+2][1]=="LAB" or token[index+2][1]=="LCB" or token[index+2][1]=="NUM" or token[index+2][1]=="ID"): #blm tau apakah perbandingan dgn id diaccept atau tidak
                            print_error(token)

                        else:
                            if (index+3)<len(token):
                                if (token[index+3][1]=="EQ"):
                                    print_error(token)

                    else:
                        print_error(token)

                elif (token[index+1][1]=="ADD"):
                    if (index+2)<len(token):
                        if not(token[index+2][1]=="LP" or token[index+2][1]=="LAB" or token[index+2][1]=="LCB" or token[index+2][1]=="STRING" or token[index+2][1]=="NUM" or token[index+2][1]=="ID"):
                            print_error(token)
                        else:
                            if (index+3)<len(token):
                                if (token[index+3][1]=="EQ"):
                                    print_error(token)


                    else:
                        print_error(token)
            '''
            else:
                if (index-1)>=0:
                    if not(token[index-1][1]=="RETURN" or token[index-1][1]=="AS" or token[index-1][1]=="IMPORT" or token[index-1][1]=="LP" or token[index-1][1]=="LCB" or token[index-1][1]=="LAB" or token[index-1][1]=="IF" or token[index-1][1]=="ELIF"  or token[index-1][1]=="ARROW" or token[index-1][1]=="COLON" or token[index-1][1]=="EQ" or token[index-1][1]=="NEQ" or token[index-1][1]=="ISEQ" or token[index-1][1]=="MUKEQ" or token[index-1][1]=="MINEQ" or token[index-1][1]=="ADDEQ" or token[index-1][1]=="ADD" or token[index-1][1]=="MUL" or token[index-1][1]=="SUB" or token[index-1][1]=="SUB" or token[index-1][1]=="SUB"):
                        print_error(token)
            '''

        if token[index][1]=="NUM":
            if (index+1)<len(token):
                if token[index+1][1]=="ID":
                    print_error(token)

                elif (token[index+1][1]=="ADD" or token[index+1][1]=="SUB" or token[index+1][1]=="MUL" or token[index+1][1]=="POWER" or token[index+1][1]=="DIV" or token[index+1][1]=="LESS" or token[index+1][1]=="LEQ" or token[index+1][1]=="GREATER"  or token[index+1][1]=="GEQ"):
                    if (index+2)<len(token):
                        if token[index+2][1]!=("NUM"):
                            print_error(token)

                        else:
                            if (index+3)<len(token):
                                if (token[index+3][1]=="EQ"):
                                    print_error(token)
                    else:
                        print_error(token)


        index+=1

def print_error(token):
    print("Syntax Error\nError at expression:", end=" ")
    for elmt in token:
        print(elmt[0], end="")