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
    return flag

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operator = ['+', '-', '*' , '/', '<', '>', '%', '^', '&', '>>>', 
            '<<', '>>', '|', '~', '==', '>=', '<=', '===', '!=', '!==',
            '&&', '||', '!', '??', '**']
single_operator = ['+', '-', '*', '/', '<', '>', '%', '^', '&', '>',
                    '<', '|', '~', '=', '!', '?']

def check_arithmetic_expression(input : str) -> bool:
    # Menghapus spasi
    input = input.replace(' ', '')
    if(input[0] in single_operator):
        return False
    else:
        return q0(input)

def q0(input : str) -> bool:
    if (len(input) == 0):
        return True
    else:
        if (input[0] in digits):
            return q0(input[1:])
        elif (input[0] == '.'):
            return q1(input[1:])
        elif (input[0] in single_operator):
            return q2(input)
        else:
            return False
        
def q1(input : str) -> bool:
    if (len(input) == 0):
        return True
    else:
        if(input[0] in digits):
            return q1(input[1:])
        elif(input[0] in single_operator):
            return q2(input)
        else:
            return False

# Cek expression
def q2(input : str) -> bool:
    if(len(input) == 0):
        return False
    else:
        firstChar = input[0]
        if (firstChar == '<'):
            if(len(input) > 2):
                if(input[1] == '<' or input[1] == '='):
                    return q0(input[2:])
            if (len(input) > 1):
                return q0(input[1:])

        elif (firstChar == '>'):
            if(len(input) > 3):
                if(input[1] == '>' and input[2] == '>'):
                    return q0(input[3:])
            if (len(input) > 2):
                if(input[1] == '>' or input[1] == '='):
                    return q0(input[2:])
            if (len(input) > 1):
                return q0(input[1:])

        elif (firstChar == '|'):
            if(len(input) > 2):
                if(input[1] == '|'):
                    return q0(input[2:])
            if(len(input) > 1):
                return q0(input[1:])

        elif (firstChar == '?'):
            if(len(input) > 2):
                if(input[1] == '?'):
                    return q0(input[2:])
            if(len(input) > 1):
                return q0(input[1:])

        elif (firstChar == '!'):
            return q2(input[1:])

        elif (firstChar == '~'):
            return q2(input[1:])

        elif (firstChar == '*'):
            if(len(input) > 2):
                if(input[1] == '*'):
                    return q0(input[2:])
            if(len(input) > 1):
                return q0(input[1:])

        elif (firstChar == '='):
            if(len(input) > 3):
                if(input[1] == '=' and input[2] == '='):
                    return q0(input[3:])
            if (len(input) > 2):
                if(input[1] == '='):
                    return q0(input[2:])
            if (len(input) > 1):
                return q0(input[1:])

        elif (firstChar == '/'):
            ...
            
        elif (firstChar == '+' or firstChar == '-' or firstChar == '^' or firstChar == '%'):
            return q0(input[1:])

        elif (firstChar in digits or firstChar == '.'):
            if(firstChar in digits):
                return q0(input[1:])
            else:
                return q1(input[1:])
        else:
            return False

# Kasus OPERATOR baru ~ ato ! harus expression dulu, OPERATOR sendiri tanpa angka

print(check_arithmetic_expression('1 + 1'))