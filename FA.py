canBeFirstChar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                  '_', '$']

# State finalnya adalah ketika first character dari string adalah huruf alfabet, _, dan $.
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
# operator   = "+" | "-" | "*" | "/" | "<" | ">"
# expression = number { operator number }

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operator = ['+', '-', '*' , '/', '<', '>' , '%', '^', '&', '>>>', 
            '<<', '>>', '|', '~', '==', '>=', '<=', '===', '!=', '!==',
            '&&', '||', '!', '??']

# Note: Perlu cek bilangan koma, kalo < bedain sama <<, sama >, >>, >>>
# Expression: Number {Operator} Number

def check_arithmetic_expression(input):
    # Menghapus spasi
    input = input.replace(' ', '')

def q0(input) -> bool:
    if (len(input) == 0):
        print("Woi")
        return True
    if(input[0] == '.'):
        q1(input[1:])
    if (input[0] in digits):
        q0(input[1:])

def q1(input):
    firstChar = input[0]
    if(firstChar == '.'):
        return False
    else:
        for char in digits:
            if (firstChar == char):
                q0(input[1:])

def q2(input):
    ...
    # Cek expression

print(q0('12'))