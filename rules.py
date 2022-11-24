import re
import sys
# list token untuk syntax ke token
token_exp = [  
    (r'[ \t]+',                                      None),                         # Tab char
    (r'\/\/ [^\n]*',                                 None),                         # single line comment
    (r'[\n]+ [ \t]* \/\* [(?!(\'\'\'))\w\W]* \*\/',  None),                         # /* multi line comment*/

    # Integer and String
    (r'\"[^\"\n]*\"',               "STRING"),                          # "string"  (apapun yang bukan " dan string)    
    (r'\'[^\'\n]*\'',               "STRING"),                          # 'string'
    (r'[\+\-]?[0-9]*\.[0-9]+',          "NUM"),                             # membaca float (boleh diberikan + atau -), boleh tidak ada angka depan koma (e.g. -.9, +.34, +64,7) 
    (r'[\+\-]?[1-9][0-9]+',             "NUM"),                             # membaca int, untuk 2 angka atau lebih
    (r'[\+\-]?[0-9]',                   "NUM"),                             # membaca int untuk tepat satu angka

    # Delimiter
    (r'\n',                             "NEWLINE"),                             
    (r'\(',                             "KBKI"),                            # Kurung Biasa kiri
    (r'\)',                             "KBKA"),                            # Kurung biasa kanan
    (r'\[',                             "KSKI"),                            # Kurung Siku KIri
    (r'\]',                             "KSKA"),                            # Kurung Siku kanan
    (r'\{',                             "KKKI"),                            # Kurung Kurawal Kiri
    (r'\}',                             "KKKA"),                            # Kurung kurawal kanan
    (r'\;',                             "TITIKKOMA"),                       
    (r'\:',                             "TITIKDUA"),

    # Operator
    # Arithmatical Operator
    (r'\+\=',                      "ADDAS"),
    (r'\+\+',                      "INCREMENT"),
    (r'\+',                         "ADD"),
    (r'\-',                         "SUB"),
    (r'\-\=',                      "SUBAS"),
    (r'\-\-',                      "DECREMENT"),
    (r'\*',                         "MUL"),
    (r'\*\=',                      "MULAS"),
    (r'\/',                         "DIV"),
    (r'\/\=',                      "DIVAS"),
    (r'\%',                         "MOD"),
    (r'\%\=',                      "MODAS"),
    (r'\*\*\=',                   "POWAS"),                    
    (r'\*\*',                      "POW"),
    (r'\/\/\=',                   "FLOORDIVAS"),
    (r'\/\/',                      "FLOORDIV"),
    # Function Operator
    (r'\=\>',                      "ARROW"),
    # Logical Operator
    (r'\<\=',                      "LEQ"),
    (r'\<',                         "L"),
    (r'\>\=',                      "GEQ"),
    (r'\>',                         "G"),
    (r'\!\=',                      "NEQ"),
    (r'\=\=',                      "ISEQ"),
    (r'\=(?!\=)',                   "EQ"),
    (r'\&\&',                      "AND"),
    (r'\|\|',                      "OR"),
    (r'\!',                         "NOT"),

    # Keyword
    # (r'\bformat\b',             "FORMAT"),
    (r'\bif\b',                 "IF"),
    (r'\belse\b',               "ELSE"),
    (r'\belse if\b',            "ELSE IF"),  # aaaa

    (r'\bfor\b',                "FOR"), 
    (r'\bin\b',                 "IN"),
    (r'\bof\b',                 "OF"), 

    (r'\bdo\b',                 "DO"),
    (r'\bwhile\b',              "WHILE"),

    (r'\bswitch\b',             "SWITCH"),
    (r'\bcase\b',               "CASE"),
    (r'\bdefault\b',            "DEFAULT"), 

    (r'\btry\b',                "TRY"),
    (r'\bcatch\b',              "CATCH"),
    (r'\bfinally\b',            "FINALLY"),
    (r'\bthrow\b',              "THROW"),
    (r'\bdelete\b',             "DELETE"),

    (r'\bcontinue\b',           "CONTINUE"), 
    (r'\bbreak\b',              "BREAK"), 

    (r'\bfalse\b',                   "FALSE"),
    (r'\btrue\b',                    "TRUE"),
    (r'\bnull\b',                    "NULL"),
    (r'\bundefined\b',               "UNDEFINED"),

    (r'\bclass\b',              "CLASS"),
    (r'\bfunction\b',           "FUNCTION"),
    (r'\breturn\b',             "RETURN"),
    (r'\bextends\b',             "EXTENDS"),
    # (r'\bconstructor\b',        "CONSTRUCTOR"),
    (r'\bnew\b',                "NEW"),

    (r'\bfrom\b',               "FROM"),
    (r'\bimport\b',             "IMPORT"),
    (r'\bas\b',                 "AS"),

    (r'\braise\b',              "RAISE"),
    (r'\bwith\b',               "WITH"),

    (r'\bnull\b',               "NULL"),
    (r'\blet\b',                "TYPE"),
    (r'\bvar\b',                "TYPE"),
    (r'\bconst\b',              "TYPE"),

    (r'\bthis.[A-Za-z_][A-Za-z0-9_]*\b',                  "ID"),
    (r'\,',                     "COMMA"),
    (r'\w+([.]\w+)+',              "ID"),
    (r'\.',                     "TITIK"),
    (r'\bis\b',                 "IS"),
    

    (r'\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',       "MULTILINE"),
    (r'\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',       "MULTILINE"),
    (r'[A-Za-z_][A-Za-z0-9_]*',                 "ID"),
    
    # (r'\brange\b',              "RANGE"), 
    # (r'\bthen\b',               "THEN"),


    # (r'\bdict\b',               "TYPE"),
    # (r'\bint\b',                "TYPE"),
    # (r'\bstr\b',                "TYPE"),
    # (r'\bfloat\b',              "TYPE"),
    # (r'\bcomplex\b',            "TYPE"),
    # (r'\blist\b',               "TYPE"),
    # (r'\btuple\b',              "TYPE"),
    # (r'\bset\b',                "TYPE"),
]

"""
Keterangan:
\               -> setiap pembacaan karakter diawali dengan ini, contoh pembacaan "a", maka \a
^               -> tanda negasi
? (e.g. a?b)    -> a cuma boleh muncul sekali atau tidak sama sekali
+ (e.g. a+)     -> repetisi muncul a, minimal a muncul sekali (tidak boleh epsilon)
* (e.g. a*)     -> repetisi muncul a, boleh epsilon
x(?!y)          -> munculnya karakter x tidak boleh diikuti oleh y

"""

def lexer(input, token_exp):
    posAbs = 0 # Menggambarkan posisi absolute terhadap posisi start file
    posRel = 1 # Menggambarkan posisi relative terhadap new line
    line = 1 # Menggambarkan banyaknya jumlah line dalam file 

    # Array untuk menampung token yang dibaca dari file
    tokenResult = []

    #Membaca file sampai selesai 
    while(posAbs < len(input)):
        #Jika membaca new line, posRel direset ke 1 dan jumlah line bertambah 1
        if(input[posAbs] == '\n'):
            posRel = 1
            line +=1
        match = None

        # Looping token di dalam token_exp
        for token in token_exp:
            # Pecah token menjadi pattern dan tag (tag = Nama token)
            pattern,tag = token
            # Mengubah string di regex menjadi sebuah pattern dalam bentuk regex
            regex = re.compile(pattern)

            # isMatched bernilai benar kalau ada regex yang sama dengan value atau kata yang dibaca 
            isMatched = regex.match(input,posAbs)

            #Jika ada regex yang memenuhi value, cek value tag
            if(isMatched):
                #Jika tag tidak bernilai None, masukan tag ke dalam token result
                if (tag):
                    tokenResult.append(tag)
                break #break kalau sudah ketemu dan terjadi akuisisi, sehingga tidak melanjutkan looping sampai token_exp terakhir
        
        #Kalau misalnya tidak ada regex yang memenuhi value yang sedang dibaca
        if not isMatched : 
            #Syntax salah dan program pasti salah
            print('Illegal Move')
            print("Sytax ERROR")
            sys.exit(1)
        else:
            posAbs = isMatched.end(0) #pindahin pos ke akhir pembacaan value yang matched dengan regex
        posRel += 1
    #Mengembalikan token result
    return tokenResult

def createToken(namaFile):
    file = open(namaFile)
    input = file.read()
    file.close()
    return(lexer(input,token_exp))

createToken('tes.js')
    