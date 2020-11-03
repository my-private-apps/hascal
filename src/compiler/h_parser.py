# -----------------------------------
# | Hascal Compiler v1.2 --- Parser |
# -----------------------------------

from core import Parser
from lexer import Lexer
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

    @_('IMPORT STRING SEM')
    def statement(self, p):
        self.src_imports += "\n#include \"{0}.h>\" \n".format(p.STRING)
    @_('USE STRING SEM')
    def statement(self, p):
        with open(p.STRING, 'r') as f:
            print("compiling use")
            parser = Parser()
            parser.parse(Lexer().tokenize(f.read()))
            self.src_before_main += '\n' + parser.src_before_main
    #@_('USE STRING SEM')
    #def statement(self, p):
    #    self.src_imports += "\n#include <{0}.h>\n".format(p.STRING)
    @_('statements')
    def statements(self, p):
        self.src_imports += p.statements
# Functions
#_____________________________        
    @_('var_assigns')
    def in_statement(self, p):
        return p.var_assigns        
    #--------------------------------------                   
    @_('call_funcs_params')
    def in_statement(self, p):
        return p.call_funcs_params
    @_('call_funcs')
    def in_statement(self, p):
        return p.call_funcs
    #--------------------------------------
    @_('const_declares')
    def in_statement(self, p):
        return p.const_declares
    #------------------------
    @_('ccodes')
    def in_statement(self, p):
        return p.ccode
    #------------------------------------------
    @_('if_stmts')
    def in_statement(self, p):
        return p.if_stmt
    @_('if_else_stmts')
    def in_statement(self, p):
        return p.if_else_stmt
    #--------------------------------------------
    @_('RETURN in_expr SEM')
    def in_statement(self, p):
        return str("return {0} ; ".format(p.in_expr))
    @_('RETURN STRING SEM')
    def in_statement(self, p):
        return str("return \"{0}\" ; ".format(p.STRING))
    #--------------------------------------------
    @_('reads')
    def in_statement(self, p):
        return p.reads
    #----------------------------------------------
    @_('var_assgin_after')
    def in_statement(self, p):
         return "{0}".format(p.var_assgin_after)
    #----------------------------------------------  
    @_('while_stmts')
    def in_statement(self, p):
        return p.while_stmt
    @_('for_stmts')
    def in_statement(self, p):
        return p.for_stmt
    #---------------------------------------------


#_______________________________________________________________________________________________________
    @_('funcs_params')
    def statement(self, p):
        self.src_before_main += p.funcs_params        
    @_('funcs_return')
    def statement(self, p):
        self.src_before_main += p.funcs_return
    @_('funcs_params_return')
    def statement(self, p):
        self.src_before_main += p.funcs_params_return        
    @_('funcs')
    def statement(self, p):
        self.src_before_main += p.funcs
    #-------------------------------------------
    @_('var_assigns')
    def statement(self, p):
        self.src_main += p.var_assigns        
    #-------------------------------------------
    @_('const_declares')
    def statement(self, p):
        self.src_main += p.const_declares
    #-------------------------------------------
    @_('var_assgin_after')
    def statement(self, p):
        self.src_main += "{0}".format(p.var_assgin_after)
    #-------------------------------------------
    @_('call_funcs_params')
    def statement(self, p):
        self.src_main += p.call_funcs_params
    @_('call_funcs')
    def statement(self, p):
        self.src_main += p.call_funcs
    #-------------------------------------------
    @_('reads')
    def statement(self, p):
        self.src_main += p.reads
    #-------------------------------------------
    @_('ccodes')
    def statement(self, p):
        self.src_main += p.ccodes
    #-------------------------------------------
    @_('if_stmts')
    def statement(self, p):
        self.src_main += p.if_stmts
    @_('if_else_stmts')
    def statement(self, p):
        self.src_main += p.if_else_stmts
    #-------------------------------------------
    @_('for_stmts')
    def statement(self, p):
        self.src_main += p.for_stmts
    @_('while_stmts')
    def statement(self, p):
        self.src_main += p.while_stmts

#__________________________________________________________________________________________#
#__________________________________________________________________________________________#
#__________________________________________________________________________________________#
#__________________________________________________________________________________________#
#__________________________________________________________________________________________#
#__________________________________________________________________________________________#
#__________________________________________________________________________________________#
#__________________________________________________________________________________________#
#__________________________________________________________________________________________#
#__________________________________________________________________________________________#
#__________________________________________________________________________________________#
#__________________________________________________________________________________________#
#__________________________________________________________________________________________#
#__________________________________________________________________________________________#
#__________________________________________________________________________________________#
#__________________________________________________________________________________________#
#__________________________________________________________________________________________#
#__________________________________________________________________________________________#
#__________________________________________________________________________________________#
    # Bases
    @_('statement')
    def statements(self, p):
        return p.statement
    @_('statements statement')
    def statements(self, p):
        return p.statements + p.statement
    #---------------------------------------------
    @_('NAME ASSIGN STRING SEM')
    def var_assgin_after(self, p):
        return str("{0} = \"{1}\";".format(p.NAME,p.STRING))
    @_('NAME ASSIGN expr SEM')
    def var_assgin_after(self, p):
        return str("{0} = {1};".format(p.NAME,p.expr))
    @_('NAME LBRACE expr RBRACE ASSIGN STRING SEM')
    def var_assgin_after(self, p):
        return str("{0}[{1}] = \"{2}\";".format(p.NAME,p.expr,p.STRING))
    @_('NAME LBRACE expr RBRACE ASSIGN expr SEM')
    def var_assgin_after(self, p):
        return str("{0}[{1}] = {2};".format(p.NAME,p.expr0,p.expr1))
    #---------------------------------------------

    @_('NAME params_call SEM')
    def call_func_params(self, p):
        return "{0} ({1}) ;".format(p.NAME,p.params_call)
    @_('call_func_params')
    def call_funcs_params(self, p):
        return p.call_func_params
    @_('call_funcs_params call_func_params')
    def call_funcs_params(self, p):
        return p.call_funcs_params + p.call_func_params
    @_('NAME SEM')
    def call_func(self, p):
        return "{0} () ;".format(p.NAME)
    @_('call_func')
    def call_funcs(self, p):
        return p.call_func
    @_('call_funcs call_func')
    def call_funcs(self, p):
        return p.call_funcs + p.call_func
    #----------------------------------
    @_('FOR NAME ASSIGN expr TO expr DO in_statements END SEM')
    def for_stmt(self, p):
        return str("for({0} = {1};{2} <= {3};{4}++){{{5}}}".format(p.NAME,p.expr0,p.NAME,p.expr1,p.NAME,p.in_statements))
    @_('for_stmt')
    def for_stmts(self, p):
        return p.while_stmt
    @_('for_stmts for_stmt ')
    def for_stmts(self, p):
        return p.while_stmts + p.for_stmt
    @_('WHILE expr DO in_statements END SEM')
    def while_stmt(self, p):
        return str("while({0}){{{1}}}".format(p.expr,p.in_statements))
    @_('while_stmt')
    def while_stmts(self, p):
        return p.while_stmt
    @_('while_stmts while_stmt')
    def while_stmts(self, p):
        return p.while_stmts + p.while_stmt
    #----------------------------------
    @_('IF expr THEN in_statements END SEM')
    def if_stmt(self, p):
        return"if({0}){{{1}}}".format(p.expr,p.in_statements)
    @_('if_stmt')
    def if_stmts(self, p):
        return p.if_else_stmt
    @_('if_stmts if_stmt')
    def if_stmts(self, p):
        return p.if_stmts + p.if_stmt
    
    @_('IF expr THEN in_statements ELSE in_statements END SEM')
    def if_else_stmt(self, p):
        return str("if({0}){{{1}}}else {{{2}}}".format(p.expr,p.in_statements0,p.in_statements1))
    @_('if_else_stmt')
    def if_else_stmts(self, p):
        return p.if_else_stmt
    @_('if_else_stmts if_else_stmt')
    def if_else_stmts(self, p):
        return p.if_else_stmts + p.if_else_stmt

    #----------------------------------
    @_('CCODE STRING SEM')
    def ccode(self, p):
        return "{0}".format(p.STRING)
    @_('ccode STRING SEM')
    def ccodes(self, p):
        return p.ccode
    @_('ccodes ccode')
    def ccodes(self, p):
        return p.ccodes + p.ccode
    #----------------------------------
    @_('NAME ASSIGN READSTR SEM')
    def read_str(self, p):
        return "scanf(\"%s\",&{0});".format(p.NAME)
    @_('read_str')
    def reads_str(self, p):
        return p.read_str
    @_('reads_str read_str')
    def reads_str(self, p):
        return p.reads_str + p.read_str
    
    @_('NAME ASSIGN READINT SEM')
    def read_int(self, p):
        return "scanf(\"%d\",&{0});".format(p.NAME)
    @_('read_int')
    def reads_int(self, p):
        return p.read_int
    @_('reads_int read_int')
    def reads_int(self, p):
        return p.reads_int + p.read_int

    @_('reads_int')
    def reads(self, p):
        return p.reads_int
    @_('reads_str')
    def reads(self, p):
        return p.reads_str
    @_('reads_str reads_int')
    def reads(self, p):
        return p.reads_str + p.reads_int
    @_('reads_int reads_str')
    def reads(self, p):
        return p.reads_int + p.reads_str
    @_('reads')
    def reads(self, p):
        return p.reads
    #----------------------------------
    @_('CONST NAME ASSIGN STRING SEM')
    def const_declare_str(self, p):
        return "\nconst char {0} [100000] = \"{1}\" ;".format(p.NAME,p.STRING)
    @_('const_declare_str')
    def const_declares_str(self, p):
        return p.const_declare_expr
    @_('const_declares_str const_declare_str')
    def const_declares_str(self, p):
        return p.const_declares_str + p.const_declare_str
    
    @_('CONST NAME ASSIGN expr SEM')
    def const_declare_expr(self, p):
        return "\nconst int {0} = {1} ;".format(p.NAME,p.expr)
    @_('const_declare_expr')
    def const_declares_expr(self, p):
        return p.const_declare_expr
    @_('const_declares_expr const_declare_expr')
    def const_declares_expr(self, p):
        return p.const_declares_expr + p.const_declare_expr
    
    @_('const_declare_expr')
    def const_declare(self, p):
        return p.const_declares_expr
    @_('const_declare_str')
    def const_declare(self, p):
        return p.const_declares_str
    @_('const_declare_str const_declare_expr')
    def const_declares(self, p):
        return p.const_declare_str + p.const_declare_expr
    @_('const_declare_expr const_declare_str')
    def const_declare(self, p):
        return p.const_declare_expr + p.const_declare_str
    @_('const_declares_str const_declares_expr')
    def const_declares(self, p):
        return p.const_declares_str + p.const_declares_expr
    @_('const_declare')
    def const_declares(self, p):
        return p.const_declare
    @_('const_declares const_declare')
    def const_declares(self, p):
        return p.const_declarea
    #----------------------------------
    @_('VAR NAME ASSIGN expr SEM')
    def var_assign_expr(self, p):
        return "\nint {0} = {1} ;".format(p.NAME,p.expr)
    @_('var_assign_expr')
    def var_assigns_expr(self, p):
        return p.var_assign_expr
    @_('var_assigns_expr var_assign_expr')
    def var_assigns_expr(self, p):
        return p.var_assigns_expr + p.var_assign_expr
    
    @_('VAR NAME ASSIGN STRING SEM')
    def var_assign_str(self, p):
        return "\nchar {0} [100000] = \"{1}\" ;".format(p.NAME,p.STRING)
    @_('var_assign_str')
    def var_assigns_str(self, p):
        return p.var_assign_str
    @_('var_assigns_str var_assigns_str')
    def var_assigns_str(self, p):
        return p.var_assigns_str + p.var_assign_str

    @_('var_assign_str')
    def var_assign(self, p):
        return p.var_assign_str
    @_('var_assign_expr')
    def var_assign(self, p):
        return p.var_assign_expr
    @_('var_assign_expr var_assign_str')
    def var_assign(self, p):
        return p.var_assign_expr + p.var_assign_str
    @_('var_assign_str var_assign_expr')
    def var_assign(self, p):
        return p.var_assign_str + p.var_assign_expr
    @_('var_assigns_expr var_assigns_str')
    def var_assigns(self, p):
        return p.var_assigns_expr + p.var_assigns_str
    @_('var_assigns_str var_assigns_expr')
    def var_assigns(self, p):
        return p.var_assigns_str + p.var_assigns_expr
    @_('var_assigns var_assign')
    def var_assigns(self, p):
        return p.var_assigns
    #----------------------------------
    @_('FUNCTION NAME DOTDOT params in_statements END SEM')
    def func_params(self, p):
        return "void {0} ({1}) {{{2}}}".format(p.NAME,p.params,p.in_statements)
    @_('func_params')
    def funcs_params(self, p):
        return p.func_params
    @_('funcs_params func_params')
    def funcs_params(self, p):
        return p.funcs_params + p.func_params
    
    @_('FUNCTION NAME AS return_type in_statements END SEM')
    def func_return(self, p):
        return "{0} {1} (void) {{{2}}}".format(p.return_type,p.NAME,p.in_statements)
    @_('func_return')
    def funcs_return(self, p):
        return p.func_return
    @_('funcs_return func_return')
    def funcs_return(self, p):
        return p.funcs_return + p.func_return
    
    @_('FUNCTION NAME DOTDOT params AS return_type in_statements END SEM')
    def func_params_return(self, p):
        return "{0} {1} ({2}) {{{3}}}".format(p.return_type,p.NAME,p.params,p.in_statements)
    @_('func_params_return')
    def funcs_params_return(self, p):
        return p.func_params_return
    @_('funcs_params_return func_params_return')
    def funcs_params_return(self, p):
        return p.funcs_params_return + p.func_params_return
    
    @_('FUNCTION NAME in_statements END SEM')
    def func(self, p):
        return "void {0} (void) {{{1}}}".format(p.NAME,p.in_statements)
    @_('func')
    def funcs(self, p):
        return p.func
    @_('funcs func')
    def funcs(self, p):
        return p.funcs + p.func

    @_('func')
    def all_func(self, p):
        return  p.func
    @_('func_params_return')
    def all_func(self, p):
        return  p.func_params_return
    @_('func_return')
    def all_func(self, p):
        return  p.func_return
    @_('func_params')
    def all_func(self, p):
        return  p.func_params
    @_('funcs')
    def all_func(self, p):
        return  p.funcs
    @_('funcs_params_return')
    def all_func(self, p):
        return  p.funcs_params_return
    @_('funcs_return')
    def all_func(self, p):
        return  p.funcs_return
    @_('funcs_params')
    def all_func(self, p):
        return  p.funcs_params
    @_('all_func')
    def all_funcs(self, p):
        return  p.all_func
    @_('all_funcs all_func')
    def all_funcs(self, p):
        return  p.all_funcs + p.all_func
    #-----------------------------------




    
    @_('statement')
    def statement(self, p):
        return p.statement
    @_('expr')
    def statement(self, p):
        return p.expr    
    @_('expr PLUS expr')
    def expr(self, p):
        return p.expr0 + p.expr1
    @_('expr MINUS expr')
    def expr(self, p):
        return p.expr0 - p.expr1
    @_('expr TIMES expr')
    def expr(self, p):
        return p.expr0 * p.expr1
    @_('expr DIVIDE expr')
    def expr(self, p):
        return p.expr0 / p.expr1
    @_('MINUS expr %prec UMINUS')
    def expr(self, p):
        return -p.expr
    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr
    @_('NUMBER')
    def expr(self, p):
        return int(p.NUMBER)
    @_('NAME')
    def expr(self, p):
        return p.NAME
    @_('NAME LBRACE expr RBRACE')
    def str_andis(self, p):
        return str("{0}[{1}]".format(p.NAME,p.expr))
#If Expr(s)    
    @_('expr EQEQ expr')
    def expr(self, p):
        return str("{0} == {1}".format(p.expr0,p.expr1))    
    @_('expr NOTEQ expr')
    def expr(self, p):
        return str("{0} != {1}".format(p.expr0,p.expr1))
    
    @_('expr LESSEQ expr')
    def expr(self, p):
        return str("{0} <= {1}".format(p.expr0,p.expr1))
    
    @_('expr GREATEREQ expr')
    def expr(self, p):
        return str("{0} >= {1}".format(p.expr0,p.expr1))

    
    @_('expr LESS expr')
    def expr(self, p):
        return str("{0} < {1}".format(p.expr0,p.expr1))

    @_('expr GREATER expr')
    def expr(self, p):
        return str("{0} > {1}".format(p.expr0,p.expr1))

    
#End If Expr(s)    
    @_('params COMMA param')
    def params(self, p):
        return p.params +","+ p.param

    @_('param')
    def params(self, p):
        return p.param

    
    @_('INTVAR NAME')
    def param(self, p):
        return p.INTVAR+" "+ p.NAME
    @_('STRINGVAR NAME')
    def param(self, p):
        return p.STRINGVAR +" "+ p.NAME

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
    @_('NAME')
    def param_call(self, p):
        return p.NAME
    
    @_('STRINGVAR')
    def return_type(self, p):
        return "char[]"
    @_('INTVAR')
    def return_type(self, p):
        return "int"
#________Function_____________
    @_('in_statement')
    def in_statements(self, p):
        return p.in_statement
    @_('in_statements in_statement')
    def in_statements(self, p):
        return p.in_statements + p.in_statement
    @_('in_statement')
    def in_statement(self, p):
        return p.in_statement
    
    @_('in_expr')
    def in_statement(self, p):
        return p.in_expr
    @_('in_expr PLUS in_expr')
    def in_expr(self, p):
        return p.in_expr0 + p.in_expr1

    @_('in_expr MINUS in_expr')
    def in_expr(self, p):
        return p.in_expr0 - p.in_expr1

    @_('in_expr TIMES in_expr')
    def in_expr(self, p):
        return p.in_expr0 * p.in_expr1

    @_('in_expr DIVIDE in_expr')
    def in_expr(self, p):
        return p.in_expr0 / p.in_expr1

    @_('MINUS in_expr %prec UMINUS')
    def in_expr(self, p):
        return -p.in_expr

    @_('LPAREN expr RPAREN')
    def in_expr(self, p):
        return p.in_expr
    @_('STRING')
    def in_expr(self, p):
        return p.STRING
    
    @_('NUMBER')
    def in_expr(self, p):
        return p.NUMBER
    @_('NAME')
    def in_expr(self, p):
        return p.NAME
    #If Expr(s)    
    @_('in_expr EQEQ in_expr')
    def in_expr(self, p):
        return str("{0} == {1}".format(p.in_expr0,p.in_expr1))
    
    @_('in_expr NOTEQ in_expr')
    def in_expr(self, p):
        return str("{0} != {1}".format(p.in_expr0,p.in_expr1))
    
    @_('in_expr LESSEQ in_expr')
    def in_expr(self, p):
        return str("{0} <= {1}".format(p.in_expr0,p.in_expr1))
    
    @_('in_expr GREATEREQ in_expr')
    def in_expr(self, p):
        return str("{0} >= {1}".format(p.in_expr0,p.in_expr1))
    
    @_('in_expr LESS in_expr')
    def in_expr(self, p):
        return str("{0} < {1}".format(p.in_expr0,p.in_expr1))

    @_('in_expr GREATER in_expr')
    def in_expr(self, p):
        return str("{0} > {1}".format(p.in_expr0,p.in_expr1))
#End If Expr(s)    
#_________End_Function_______________
