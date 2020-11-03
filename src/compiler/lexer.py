# -----------------------------------
# | Hascal Compiler v1.2 --- Lexer |
# -----------------------------------

from core import Lexer
class Lexer(Lexer):
    tokens = {
        NAME,
        FOR,
        WHILE,
        DO,
        TO,
        IF,
        THEN,
        ELSE,
        RETURN,
        FLOAT,
        AS,
        INTVAR,
        STRINGVAR,
        GREATER,
        LESS,
        EQEQ,
        NOTEQ,
        GREATEREQ,
        LESSEQ,
        NUMBER,
        PLUS,
        TIMES,
        CCODE,
        MINUS,
        DIVIDE,
        ASSIGN,
        COMMA,
        LPAREN,
        RPAREN,
        DOTDOT,
        VAR,
        SEM,
        STRING,
        USE,
        FUNCTION,
        CONST,
        READSTR,
        READINT,
        READFLOAT,
        IMPORT,
        LBRACE,
        RBRACE,
        END
        }
    literals = {'.'}
    ignore = ' \t'
    # Tokens
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'

    # Special symbols
    PLUS = r'\+'
    EQEQ = r'=='
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    ASSIGN = r'='
    LPAREN = r'\('
    RPAREN = r'\)'
    SEM = r';'
    DOTDOT = r':'
    COMMA = r','
    NOTEQ = r'!='
    LESSEQ = r'<='
    GREATEREQ = r'>='
    LESS = r'<'
    GREATER = r'>'
    LBRACE = r'\['
    RBRACE = r'\]'
    NAME["ccode"] = CCODE
    NAME["var"] = VAR
    NAME["use"] = USE
    NAME["function"] = FUNCTION
    NAME["end"] = END
    NAME["int"] = INTVAR
    NAME["str"] = STRINGVAR
    NAME["if"] = IF
    NAME["then"] = THEN
    NAME["else"] = ELSE
    NAME["return"] = RETURN
    NAME["as"] = AS
    NAME["for"] = FOR
    NAME["do"] = DO
    NAME["to"] = TO
    NAME["while"] = WHILE
    NAME["import"] = IMPORT
    NAME["const"] = CONST
    NAME["ReadStr"] = READSTR
    NAME["ReadInt"] = READINT
    NAME["ReadFloat"] = READFLOAT
    NAME["import"] = IMPORT
    #Ignored pattern
    #ignore_newline = r'\n+'

    # Extra action for newlines
    #def ignore_newline(self, t):
    #    self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
    @_(r'\d+\.\d+')
    def FLOAT(self, t):
        """
        Parsing float numbers
        """
        t.value = float(t.value)
        return t
    
    @_(r'\".*?(?<!\\)(\\\\)*\"')
    def STRING(self, t):
        t.value = t.value[1:-1]
        t.value = t.value.replace(r"\n", "\n")
        t.value = t.value.replace(r"\t", "\t")
        t.value = t.value.replace(r"\\", "\\")
        t.value = t.value.replace(r"\"", "\"")
        t.value = t.value.replace(r"\a", "\a")
        t.value = t.value.replace(r"\b", "\b")
        t.value = t.value.replace(r"\r", "\r")
        t.value = t.value.replace(r"\t", "\t")
        t.value = t.value.replace(r"\v", "\v")
        return t
