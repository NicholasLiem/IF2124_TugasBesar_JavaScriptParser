# list token untuk syntax ke token
token_exp = [  
    (r'[ \t]+',                     None),                          # Tab char
    (r'\/\/ [^\n]*',                None),                          # single line comment
    (r'[\n]+ [ \t]* \/\* [(?!(\'\'\'))\w\W]* \*\/',  None),         # /* multi line comment*/

    # Integer and String
    (r'\"[^\"\n]*\"',               "STRING"),                          # "string"  (apapun yang bukan " dan string)    
    (r'\'[^\'\n]*\'',               "STRING"),                          # 'string'
    (r'[\+\-]? [0-9]* \.[0-9]+',    "NUM"),                             # membaca float (boleh diberikan + atau -), boleh tidak ada angka depan koma (e.g. -.9, +.34, +64,7) 
    (r'[\+\-]?[1-9][0-9]+',         "NUM"),                             # membaca int, untuk 2 angka atau lebih
    (r'[\+\-]?[0-9]',               "NUM"),                             # membaca int untuk tepat satu angka

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
    (r'\* \* \=',                   "POWAS"),                        
    (r'\* \*',                      "POW"),
    (r'\/ \/ \=',                   "FLOORDIVAS"),
    (r'\/ \/',                      "FLOORDIV"),
    (r'\* \=',                      "MULAS"),
    (r'\/ \=',                      "DIVAS"),
    (r'\+ \=',                      "ADDAS"),
    (r'\- \=',                      "SUBAS"),
    (r'\% \=',                      "MODAS"),
    (r'\- \>',                      "ARROW"),
    (r'\+',                         "ADD"),
    (r'\-',                         "SUB"),
    (r'\*',                         "MUL"),
    (r'\/',                         "DIV"),
    (r'\%',                         "MOD"),
    (r'\< \=',                      "LEQ"),
    (r'\<',                         "L"),
    (r'\> \=',                      "GEQ"),
    (r'\>',                         "G"),
    (r'\! \=',                      "NEQ"),
    (r'\= \=',                      "ISEQ"),
    (r'\=(?!\=)',                   "EQ"),
    (r'\& \&',                      "AND"),
    (r'\| \|',                      "OR"),
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
    (r'\bcontinue\b',           "DEFAULT"), 

    (r'\btry\b',                "TRY"),
    (r'\bcatch\b',              "CATCH"),
    (r'\bfinally\b',            "FINALLY"),
    (r'\bthrow\b',              "THROW"),
    (r'\bdelete\b',             "DELETE"),

    (r'\bcontinue\b',           "CONTINUE"), 
    (r'\bbreak\b',              "BREAK"), 

    (r'\bfalse\b',              "FALSE"),
    (r'\btrue\b',               "TRUE"),

    (r'\bclass\b',              "CLASS"),
    (r'\bfunction\b',           "FUNCTION"),
    (r'\breturn\b',             "RETURN"),

    (r'\bfrom\b',               "FROM"),
    (r'\bimport\b',             "IMPORT"),
    (r'\bas\b',                 "AS"),

    (r'\braise\b',              "RAISE"),
    (r'\bwith\b',               "WITH"),

    (r'\bnull\b',               "NULL"),
    (r'\blet\b',                "TYPE"),
    (r'\bvar\b',                "TYPE"),
    (r'\bconst\b',              "TYPE"),

    (r'\,',                     "COMMA"),
    (r'\w+[.]\w+',              "KARTITIK"),
    (r'\.',                     "TITIK"),
    (r'\bis\b',                 "IS"),

    (r'\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',       "MULTILINE"),
    (r'\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',       "MULTILINE"),
    (r'[A-Za-z_][A-Za-z0-9_]*', "ID"),

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

def createToken(namaFile):
    file = open(namaFile)
    character = file.read()
    file.close()
    