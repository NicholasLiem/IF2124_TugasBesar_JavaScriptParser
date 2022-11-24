canBeFirstChar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                  '_', '$']

def check_var(input):
    flag = False
    firstChar = input[0]
    for char in canBeFirstChar:
        if (firstChar == char):
            flag = True
    if (input == 'false' or input == 'true'):
        flag = False
    return flag

# EBNF Form
# digits     = digit { digit }
# number     = [ "+" | "-" ] ( digits [ "." [ digits ] ] | "." digits )
# operator   = "+" | "-" | "*" | "/"
# expression = number { operator number }

#Regex
# digits    : [0-9]+
# number    : [+\-]?([0-9]+(\.[0-9]*)?|\.[0-9]+)
# operator  : [+\-*/]
# expression: [+\-]?([0-9]+(\.[0-9]*)?|\.[0-9]+)([+\-*/][+\-]?([0-9]+(\.[0-9]*)?|\.[0-9]+))*

def check_arithmetic_expression(input):
    ...
