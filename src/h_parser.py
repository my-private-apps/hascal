from h_lexer import Lexer
from core import Parser

class Parser(Parser):
    tokens = Lexer.tokens
    src_imports =  "#include <stdio.h>\n#include <stdlib.h> \n#include <conio.h>\n"
    src_before_main = ""
    src_all = "\
   int main(int argc, char *argv[]){ "
    src_main = " "
    src_end =  "return 0; }"
    precedence = (
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),
        ('right', UMINUS)
        )

    def __init__(self):
        self.names = { }
        

    @_('statement')
    def statements(self, p):
        return str(p.statement)
    @_('statements statements')
    def statements(self, p):
        return str(p.statements0 + p.statements1)
    @_('statements')
    def statements(self, p):
        return str(p.statements)
    @_('in_statement')
    def in_statements(self, p):
        return p.in_statement
    @_('in_statements in_statement')
    def in_statements(self, p):
        return p.in_statements + p.in_statement
    
    @_('FUNCTION NAME in_statements END SEM')
    def statement(self, p):
        self.src_before_main += "void {0} () {{{1}}}".format(p.NAME,p.in_statements)
    @_('FUNCTION NAME LPAREN params RPAREN SEM in_statements END SEM')
    def statement(self, p):
        self.src_before_main += "void {0} ({1}) {{{2}}}".format(p.NAME,p.params,p.in_statements)        
    @_('FUNCTION NAME AS return_type SEM in_statements END SEM')
    def statement(self, p):
        self.src_before_main += "{0} {1} (void) {{{2}}}".format(p.return_type,p.NAME,p.in_statements)
    @_('FUNCTION NAME LPAREN params RPAREN AS return_type SEM in_statements END SEM')
    def statement(self, p):
        self.src_before_main += "{0} {1} ({2}) {{{3}}}".format(p.return_type,p.NAME,p.params,p.in_statements)        
    @_('USE STRING SEM')
    def statement(self, p):
        path = r'libs\{0}.has'.format(p.STRING)
        with open(path, 'r') as f:
            parser = Parser()
            parser.parse(Lexer().tokenize(f.read()))
            self.src_imports += '\n'+ parser.src_imports + '\n'
            self.src_before_main += '\n'+ parser.src_before_main + '\n'
    
    @_('INTVAR NAME ASSIGN num SEM')
    def statement(self, p):
        self.src_main += "\nint {0} = {1} ;".format(p.NAME,p.num)        
    @_('STRINGVAR NAME ASSIGN STRING SEM')
    def statement(self, p):
        self.src_main += "\nchar[] {0} = \"{1}\" ;".format(p.NAME,p.STRING)
    @_('IF expr THEN in_statements END SEM')
    def statement(self, p):
        self.src_main += str("if({0}){{{1}}}".format(p.expr,p.in_statements))        
    @_('IF expr THEN in_statements ELSE in_statements END SEM')
    def statement(self, p):
        self.src_main += str("if({0}){{{1}}}else {{{2}}}".format(p.expr,p.in_statements0,p.in_statements1))
    @_('CCODE STRING  SEM')
    def statement(self, p):
        self.src_main += "{0}".format(p.STRING)
    @_('CCODE LBRACE STRING RBRACE SEM')
    def statement(self, p):
        self.src_imports += "{0}".format(p.STRING)
    @_('FOR NAME ASSIGN expr TO expr DO in_statements END SEM')
    def statement(self, p):
        self.src_main += str("for({0} = {1};{2} <= {3};{4}++){{{5}}}".format(p.NAME,p.expr0,p.NAME,p.expr1,p.NAME,p.in_statements))
    @_('WHILE expr DO in_statements END SEM')
    def statement(self, p):
        self.src_main += str("while({0}){{{1}}}".format(p.expr,p.in_statements))
    @_('NAME ASSIGN STRING SEM')
    def statement(self, p):
        self.src_main +=  str("{0} = \"{1}\";".format(p.NAME,p.STRING))
    @_('NAME ASSIGN expr SEM')
    def statement(self, p):
        self.src_main +=  str("{0} = {1};".format(p.NAME,p.expr))
    @_('NAME LBRACE expr RBRACE ASSIGN STRING SEM')
    def statement(self, p):
        self.src_main +=  str("{0}[{1}] = \"{2}\";".format(p.NAME,p.expr,p.STRING))
    @_('NAME LBRACE expr RBRACE ASSIGN expr SEM')
    def statement(self, p):
        self.src_main +=  str("{0}[{1}] = {2};".format(p.NAME,p.expr0,p.expr1))
    @_('PRINT STRING RPAREN SEM')
    def statement(self, p):
        self.src_main += str("printf(\"{0}\") ;".format(p.STRING))
    @_('PRINT LPAREN expr RPAREN SEM')
    def statement(self, p):
        self.src_main += str("printf(\"%d\",{0}) ;".format(p.expr))
    @_('PRINT LPAREN str_andis RPAREN SEM')
    def statement(self, p):
        self.src_main += "printf(\"%c\",{0}) ;".format(p.str_andis)
    @_('READSTR LPAREN NAME SEM')
    def statement(self, p):
        self.src_main += "scanf(\"%s\",&{0});".format(p.NAME)
    @_('READINT NAME SEM')
    def statement(self, p):
        self.src_main += "scanf(\"%d\",&{0});".format(p.NAME)
    @_('NAME LPAREN params_call RPAREN SEM')
    def statement(self, p):
        self.src_main += "{0}({1}) ;".format(p.NAME,p.params_call)
    @_('NAME SEM')
    def statement(self, p):
        self.src_main += "{0}() ;".format(p.NAME)
    @_('statement')
    def statement(self, p):
        self.src_main += p.statement

#########################################################
#########################################################
#########################################################
    @_('NAME params_call SEM')
    def in_statement(self, p):
        return "{0}({1}) ;".format(p.NAME,p.params_call)
    @_('NAME SEM')
    def in_statement(self, p):
        return "{0}() ;".format(p.NAME)
    #---------------------------------
    @_('READSTR NAME SEM')
    def in_statement(self, p):
        return "scanf(\"%s\",&{0});".format(p.NAME)
    @_('READINT NAME SEM')
    def in_statement(self, p):
        return "scanf(\"%d\",&{0});".format(p.NAME)
    #---------------------------------
    @_('RETURN expr SEM')
    def in_statement(self, p):
        return str("return {0} ; ".format(p.expr))
    @_('RETURN STRING SEM')
    def in_statement(self, p):
        return str("return \"{0}\" ; ".format(p.STRING))
    #---------------------------------
    @_('PRINT LPAREN STRING RPAREN  SEM')
    def in_statement(self, p):
        return str("printf(\"{0}\") ;".format(p.STRING))
    @_('PRINT LPAREN expr RPAREN SEM')
    def in_statement(self, p):
        return str("printf(\"%d\",{0}) ;".format(p.expr))
    @_('PRINT LPAREN str_andis RPAREN SEM')
    def in_statement(self, p):
        return "printf(\"%c\",{0}) ;".format(p.str_andis)
    #---------------------------------
    @_('NAME LBRACE expr RBRACE ASSIGN STRING SEM')
    def in_statement(self, p):
        return str("{0}[{1}] = \"{2}\";".format(p.NAME,p.expr,p.STRING))
    @_('NAME LBRACE expr RBRACE ASSIGN expr SEM')
    def in_statement(self, p):
        return str("{0}[{1}] = {2};".format(p.NAME,p.expr0,p.expr1))
    @_('NAME ASSIGN STRING SEM')
    def in_statement(self, p):
        return str("{0} = \"{1}\";".format(p.NAME,p.STRING))
    @_('NAME ASSIGN expr SEM')
    def in_statement(self, p):
        return str("{0} = {1};".format(p.NAME,p.expr))
    #---------------------------------
    @_('FOR NAME ASSIGN expr TO expr DO in_statements END SEM')
    def in_statement(self, p):
        return str("for({0} = {1};{2} <= {3};{4}++){{{5}}}".format(p.NAME,p.expr0,p.NAME,p.expr1,p.NAME,p.in_statements))
    @_('WHILE expr DO in_statements END SEM')
    def in_statement(self, p):
        return str("while({0}){{{1}}}".format(p.expr,p.in_statements))
    #---------------------------------
    @_('INTVAR NAME ASSIGN num SEM')
    def in_statement(self, p):
        return "\nint {0} = {1} ;".format(p.NAME,p.num)        
    @_('STRINGVAR NAME ASSIGN STRING SEM')
    def in_statement(self, p):
        return "\nchar[] {0} = \"{1}\" ;".format(p.NAME,p.STRING)
    #---------------------------------
    @_('IF expr THEN in_statements END SEM')
    def in_statement(self, p):
        return str("if({0}){{{1}}}".format(p.expr,p.in_statements))        
    @_('IF expr THEN in_statements ELSE in_statements END SEM')
    def in_statement(self, p):
        return str("if({0}){{{1}}}else {{{2}}}".format(p.expr,p.in_statements0,p.in_statements1))
    #---------------------------------
    @_('CCODE STRING  SEM')
    def in_statement(self, p):
        return "{0}".format(p.STRING)
    #----------------------------------
#---------------------------------------------#
#   Expertions                                #
#---------------------------------------------#
    @_('expr PLUS expr')
    def expr(self, p):
        return str(p.expr0 +"+"+ p.expr1)

    @_('expr MINUS expr')
    def expr(self, p):
        return str(p.expr0 +"-"+ p.expr1)

    @_('expr TIMES expr')
    def expr(self, p):
        return str(p.expr0 +"*"+ p.expr1)

    @_('expr DIVIDE expr')
    def expr(self, p):
        return str(p.expr0 +"/"+ p.expr1)

    @_('MINUS expr %prec UMINUS')
    def expr(self, p):
        return ""

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return p.NUMBER
    @_('NAME')
    def expr(self, p):
        return p.NAME
    @_('expr EQEQ expr')
    def expr(self, p):
        return str("{0} == {1}".format(p.expr0,p.expr1))
    @_('NAME EQEQ expr')
    def expr(self, p):
        return str("{0} == {1}".format(p.NAME,p.expr))
    @_('NAME EQEQ NAME')
    def expr(self, p):
        return str("{0} == {1}".format(p.NAME0,p.NAME1))
    @_('expr EQEQ NAME')
    def expr(self, p):
        return str("{0} == {1}".format(p.expr,p.NAME))
    
    @_('expr NOTEQ expr')
    def expr(self, p):
        return str("{0} != {1}".format(p.expr0,p.expr1))
    @_('NAME NOTEQ expr')
    def expr(self, p):
        return str("{0} != {1}".format(p.NAME,p.expr))
    @_('NAME NOTEQ NAME')
    def expr(self, p):
        return str("{0} != {1}".format(p.NAME0,p.NAME1))
    @_('expr NOTEQ NAME')
    def expr(self, p):
        return str("{0} != {1}".format(p.expr,p.NAME))
    
    @_('expr LESSEQ expr')
    def expr(self, p):
        return str("{0} <= {1}".format(p.expr0,p.expr1))
    @_('NAME LESSEQ expr')
    def expr(self, p):
        return str("{0} <= {1}".format(p.NAME,p.expr))
    @_('NAME LESSEQ NAME')
    def expr(self, p):
        return str("{0} <= {1}".format(p.NAME0,p.NAME1))
    @_('expr LESSEQ NAME')
    def expr(self, p):
        return str("{0} <= {1}".format(p.expr,p.NAME))
    
    @_('expr GREATEREQ expr')
    def expr(self, p):
        return str("{0} >= {1}".format(p.expr0,p.expr1))
    @_('NAME GREATEREQ expr')
    def expr(self, p):
        return str("{0} >= {1}".format(p.NAME,p.expr))
    @_('NAME GREATEREQ NAME')
    def expr(self, p):
        return str("{0} >= {1}".format(p.NAME0,p.NAME1))
    @_('expr GREATEREQ NAME')
    def expr(self, p):
        return str("{0} >= {1}".format(p.expr,p.NAME))
    
    @_('expr LESS expr')
    def expr(self, p):
        return str("{0} < {1}".format(p.expr0,p.expr1))
    @_('NAME LESS expr')
    def expr(self, p):
        return str("{0} < {1}".format(p.NAME,p.expr))
    @_('NAME LESS NAME')
    def expr(self, p):
        return str("{0} < {1}".format(p.NAME0,p.NAME1))
    @_('expr LESS NAME')
    def expr(self, p):
        return str("{0} < {1}".format(p.expr,p.NAME))

    @_('expr GREATER expr')
    def expr(self, p):
        return str("{0} > {1}".format(p.expr0,p.expr1))
    @_('NAME GREATER expr')
    def expr(self, p):
        return str("{0} > {1}".format(p.NAME,p.expr))
    @_('NAME GREATER NAME')
    def expr(self, p):
        return str("{0} > {1}".format(p.NAME0,p.NAME1))
    @_('expr GREATER NAME')
    def expr(self, p):
        return str("{0} > {1}".format(p.expr,p.NAME))
    @_('MINUS NUMBER')
    def num(self, p):
        return str("{0}{1}".format(p.MINUS,p.NUMBER))
    @_('NUMBER')
    def num(self, p):
        return str("{0}".format(p.NUMBER))
    @_('params_call COMMA param_call')
    def params_call(self, p):
        return str("{0} , {1}".format(p.params_call,p.param_call))
    
    @_('param_call')
    def params_call(self, p):
        return p.param_call
    @_('STRING')
    def param_call(self, p):
        return "\""+p.STRING+"\""
    @_('NUMBER')
    def param_call(self, p):
        return p.NUMBER
    @_('expr')
    def param_call(self, p):
        return p.expr
    @_('param')
    def params(self, p):
        return p.param
    
    @_('params COMMA param')
    def params(self, p):
        return p.params +","+ p.param


    
    @_('INTVAR NAME')
    def param(self, p):
        return p.INTVAR+" "+ p.NAME
    @_('STRINGVAR NAME')
    def param(self, p):
        return "char"+ p.NAME + "[]"
    
    @_('INTVAR')
    def return_type(self, p):
        return p.INTVAR
    @_('STRINGVAR')
    def return_type(self, p):
        return p.STRINGVAR
    
    @_('NAME LBRACE expr RBRACE')
    def str_andis(self, p):
        return str("{0}[{1}]".format(p.NAME,p.expr))
