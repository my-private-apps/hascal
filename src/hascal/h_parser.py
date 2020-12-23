from .h_lexer import Lexer
from .sly import Parser

class Parser(Parser):
    tokens = Lexer.tokens
    src_imports =  "typedef char* string;\n#include<stdbool.h>\n"
    src_before_main = "\n\n"
    src_all = "\n \
   int main(int argc, char *argv[]){\n "
    src_main = " "
    src_end =  "\nreturn 0;\n }"
    precedence = (
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),
        ('right', UMINUS)
        )

    def __init__(self):
        pass
        

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
    @_('FUNCTION NAME LPAREN params RPAREN in_statements END SEM')
    def statement(self, p):
        self.src_before_main += "void {0} ({1}) {{{2}}}".format(p.NAME,p.params,p.in_statements)        
    @_('FUNCTION NAME  AS return_type  in_statements END SEM')
    def statement(self, p):
        self.src_before_main += "{0} {1} (void) {{{2}}}".format(p.return_type,p.NAME,p.in_statements)
    @_('FUNCTION NAME LPAREN params RPAREN  AS return_type  in_statements END SEM')
    def statement(self, p):
        self.src_before_main += "{0} {1} ({2}) {{{3}}}".format(p.return_type,p.NAME,p.params,p.in_statements)
    #----------------------------------
    @_('USE STRING SEM')
    def statement(self, p):
        path = r'.\hlib\{0}.has'.format(p.STRING)
        with open(path, 'r') as f:
            parser = Parser()
            parser.parse(Lexer().tokenize(f.read()))
            self.src_imports += '\n'+parser.src_imports+'\n' + parser.src_before_main + '\n'

    @_('CCODE USE STRING SEM')
    def statement(self, p):
        self.src_imports += "\n#include <{0}>\n".format(p.STRING)
    #----------------------------------
    @_('struct_assign')
    def statement(self, p):
        self.src_before_main += "\n{0}\n".format(p.struct_assign)
    #----------------------------------
    @_('var_assign')
    def statement(self, p):
        self.src_main += "\n{0}\n".format(p.var_assign)        
    #----------------------------------      
    @_('const_assign')
    def statement(self, p):
        self.src_main += "\n{0}\n".format(p.const_assign)
    #----------------------------------
    @_('if_stmt')
    def statement(self, p):
        self.src_main += str("\n{0}\n".format(p.if_stmt))
    #---------------------------------
    @_('ccode')
    def statement(self, p):
        self.src_main += "{0}".format(p.ccode)
    #---------------------------------
    @_('loop_stmt')
    def statement(self, p):
        self.src_main += str("\n{0}\n".format(p.loop_stmt))
    #----------------------------------
    @_('call_func SEM')
    def statement(self, p):
        self.src_main += "\n{0};\n".format(p.call_func)
    #-----------------------------------
    @_('array_assigns')
    def statement(self, p):
        self.src_main += "\n{0}\n".format(p.array_assigns)
    #-----------------------------------
    @_('statement')
    def statement(self, p):
        self.src_main += p.statement

#########################################################
#########################################################
#########################################################
    @_('call_func SEM')
    def in_statement(self, p):
        return "\n{0};\n".format(p.call_func)
    #---------------------------------
    @_('RETURN expr SEM')
    def in_statement(self, p):
        return str("return {0} ; ".format(p.expr))
    #---------------------------------
    @_('loop_stmt')
    def in_statement(self, p):
        return str("\n{0}\n".format(p.loop_stmt))
    #---------------------------------
    @_('var_assign')
    def in_statement(self, p):
        return "\n{0}\n".format(p.var_assign)    
    #---------------------------------
    @_('const_assign')
    def in_statement(self, p):
        return "\n{0}\n".format(p.const_assign)        
    #---------------------------------
    @_('if_stmt')
    def in_statement(self, p):
        return str("\n{0}\n".format(p.if_stmt))
    #---------------------------------
    @_('ccode')
    def in_statement(self, p):
        return "{0}".format(p.ccode)
    #----------------------------------

    
#---------------------------------------------#
#   Expertions                                #
#---------------------------------------------#
    @_('MINUS expr %prec UMINUS')
    def expr(self, p):
        return ""

    @_('NUMBER')
    def expr(self, p):
        return p.NUMBER
    @_('name')
    def expr(self, p):
        return p.name
    
    
    @_('name LBRACE andis RBRACE')
    def expr(self, p):
        return "{0}{1}".format(p.name,p.andis)
    @_('call_func')
    def expr(self, p):
        return str(p.call_func)
    @_('')
    def expr(self, p):
        return ""
    @_('TRUE')
    def expr(self, p):
        return str(p.TRUE)
    @_('FALSE')
    def expr(self, p):
        return str(p.FALSE)
    @_('CHAR')
    def expr(self, p):
        return str(p.CHAR)
    @_('expr PLUS expr')
    def expr(self, p):
        return "{0}+{1}".format(p.expr0,p.expr1)

    @_('expr MINUS expr')
    def expr(self, p):
        return "{0}-{1}".format(p.expr0,p.expr1)

    @_('expr TIMES expr')
    def expr(self, p):
        return "{0}*{1}".format(p.expr0,p.expr1)

    @_('expr DIVIDE expr')
    def expr(self, p):
        return "{0}/{1}".format(p.expr0,p.expr1)


    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return "({0})".format(p.expr)

    @_('MINUS NAME')
    def expr(self, p):
        return str("{0}{1}".format(p.MINUS,p.NAME))
    @_('MINUS NUMBER')
    def num(self, p):
        return str("{0}{1}".format(p.MINUS,p.NUMBER))
    @_('NUMBER')
    def num(self, p):
        return str("{0}".format(p.NUMBER))
#---------------------------------------------#
#   End Expertions                            #
#---------------------------------------------#

#---------------------------------------------#
#   Conditions                                #
#---------------------------------------------#
    @_('expr EQEQ expr')
    def condition(self, p):
        return str("{0} == {1}".format(p.expr0,p.expr1))
    
    @_('expr NOTEQ expr')
    def condition(self, p):
        return str("{0} != {1}".format(p.expr0,p.expr1))
    
    @_('expr LESSEQ expr')
    def condition(self, p):
        return str("{0} <= {1}".format(p.expr0,p.expr1))
    
    @_('expr GREATEREQ expr')
    def condition(self, p):
        return str("{0} >= {1}".format(p.expr0,p.expr1))
    
    @_('expr LESS expr')
    def condition(self, p):
        return str("{0} < {1}".format(p.expr0,p.expr1))

    @_('expr GREATER expr')
    def condition(self, p):
        return str("{0} > {1}".format(p.expr0,p.expr1))

    @_('call_func')
    def condition(self, p):
        return str("{0}".format(p.call_func))
    @_('condition AND condition')
    def condition(self, p):
        return str("{0} && {1}".format(p.condition0,p.condition1))
    @_('condition OR condition')
    def condition(self, p):
        return str("{0} || {1}".format(p.condition0,p.condition1))


#---------------------------------------------#
#   End Conditions                            #
#---------------------------------------------#
    @_('NAME DOT NAME')
    def name(self, p):
        return str(p.NAME0+"."+p.NAME1)
    @_('NAME')
    def name(self, p):
        return str(p.NAME)

    #------------------------------
    @_('params_call COMMA param_call')
    def params_call(self, p):
        return str("{0} , {1}".format(p.params_call,p.param_call))
    
    @_('param_call')
    def params_call(self, p):
        return p.param_call
    @_('STRING')
    def param_call(self, p):
        return "\""+p.STRING+"\""
    @_('CHAR')
    def param_call(self, p):
        return p.CHAR
    @_('NUMBER')
    def param_call(self, p):
        return p.NUMBER
    @_('expr')
    def param_call(self, p):
        return p.expr
    @_('NAME LPAREN params_call RPAREN')
    def param_call(self, p):
        return "{0}({1})".format(p.NAME,p.params_call)
    @_('andis')
    def param_call(self, p):
        return "{0}".format(p.andis)
    #------------------------------
    @_('param')
    def params(self, p):
        return p.param
    
    @_('params COMMA param')
    def params(self, p):
        return p.params +","+ p.param

    @_('TRUE')
    def boolean(self, p):
        return str(p.TRUE)
    @_('FALSE')
    def boolean(self, p):
        return str(p.FALSE)
    
    @_('INTVAR NAME')
    def param(self, p):
        return p.INTVAR+" "+ p.NAME
    @_('STRINGVAR NAME')
    def param(self, p):
        return "string "+ p.NAME
    @_('BOOLVAR NAME')
    def param(self, p):
        return "bool "+ p.NAME
    @_('CHARVAR NAME')
    def param(self, p):
        return "char "+ p.NAME
    
    @_('INTVAR')
    def return_type(self, p):
        return p.INTVAR
    @_('STRINGVAR')
    def return_type(self, p):
        return "string"
    @_('CHARVAR')
    def return_type(self, p):
        return "char"
    @_('BOOLVAR')
    def return_type(self, p):
        return "bool"
    #------------------------------
    @_('expr')
    def andis_t(self, p):
        return str("{0}".format(p.expr))
    @_('andis_t')
    def andis(self, p):
        return str("[{0}]".format(p.andis_t))
    @_('andis COMMA andis_t')
    def andis(self, p):
        return str("{0}[{1}]".format(p.andis,p.andis_t))
    #------------------------------
    @_('array_list')
    def arrays_list(self, p):
        return p.array_list
    @_('arrays_list COMMA array_list ')
    def arrays_list(self, p):
        return p.arrays_list +','+ p.array_list
    
    @_('STRING')
    def array_list(self, p):
        return str("\"{0}\"".format(p.STRING))
    @_('expr')
    def array_list(self, p):
        return str("{0}".format(p.expr))
    @_('CHAR')
    def array_list(self, p):
        return str("{0}".format(p.CHAR))
    @_('boolean')
    def array_list(self, p):
        return str("{0}".format(p.CHAR))

    @_('')
    def array(self, p):
        return ""
    @_('expr')
    def array(self, p):
        return str("[{0}]".format(p.expr))
    @_('array')
    def arrays(self, p):
        return str("{0}".format(p.array))
    @_('arrays COMMA array')
    def arrays(self, p):
        return str("{0}{1}".format(p.arrays,p.array))
    #--------------------------------
    @_('INTVAR NAME ASSIGN num SEM')
    def var_assign(self, p):
        return "int {0} = {1} ;".format(p.NAME,p.num)        
    @_('STRINGVAR NAME ASSIGN STRING SEM')
    def var_assign(self, p):
        return "char {0} [] = \"{1}\" ;".format(p.NAME,p.STRING)
    @_('CHARVAR NAME ASSIGN CHAR SEM')
    def var_assign(self, p):
        return "char {0} = {1} ;".format(p.NAME,p.CHAR)
    @_('BOOLVAR NAME ASSIGN boolean SEM')
    def var_assign(self, p):
        return "bool {0} = {1} ;".format(p.NAME,p.boolean)
    
    @_('NAME NAME SEM')
    def var_assign(self, p):
        return  str("struct {0} {1};".format(p.NAME0,p.NAME1))
    
    @_('name ASSIGN STRING SEM')
    def var_assign(self, p):
        return  str("{0} = \"{1}\";".format(p.name,p.STRING))        
    @_('name ASSIGN expr SEM')
    def var_assign(self, p):
        return  str("{0} = {1};".format(p.name,p.expr))        
    @_('name LBRACE expr RBRACE ASSIGN STRING SEM')
    def var_assign(self, p):
        return  str("{0}[{1}] = \"{2}\";".format(p.name,p.expr,p.STRING))        
    @_('name LBRACE expr RBRACE ASSIGN expr SEM')
    def var_assign(self, p):
        return  str("{0}[{1}] = {2};".format(p.name,p.expr0,p.expr1))
    
    @_('name ASSIGN call_func SEM')
    def var_assign(self, p):
        return  str("{0} = {1};".format(p.name,p.call_func))        
    @_('name LBRACE expr RBRACE ASSIGN call_func SEM')
    def var_assign(self, p):
        return  str("{0}[{1}] = {2}".format(p.name,p.expr,p.call_func))

    @_('name ASSIGN arrays_list SEM')
    def var_assign(self, p):
        return  str("{0} = {{{1}}};".format(p.name,p.arrays_list))        
    #--------------------------------
    @_('CONST INTVAR NAME ASSIGN num SEM')
    def const_assign(self, p):
        return "const int {0} = {1} ;".format(p.NAME,p.num)        
    @_('CONST STRINGVAR NAME ASSIGN STRING SEM')
    def const_assign(self, p):
        return "const char {0} [] = \"{1}\" ;".format(p.NAME,p.STRING)
    @_('CONST CHARVAR NAME ASSIGN CHAR SEM')
    def const_assign(self, p):
        return "const string {0} = {1} ;".format(p.NAME,p.CHAR)
    @_('CONST BOOLVAR NAME ASSIGN boolean SEM')
    def const_assign(self, p):
        return "const bool {0} = {1} ;".format(p.NAME,p.boolean)
    #--------------------------------
    @_('INTVAR LBRACE arrays RBRACE NAME ASSIGN arrays_list SEM')
    def array_assigns(self, p):
        return "int {0} {1} = {{{2}}} ;".format(p.NAME,p.arrays,p.arrays_list)
    @_('STRINGVAR LBRACE arrays RBRACE NAME ASSIGN arrays_list SEM')
    def array_assigns(self, p):
        return "string {0} {1} = {{{2}}} ;".format(p.NAME,p.arrays,p.arrays_list)
    @_('BOOLVAR LBRACE arrays RBRACE NAME ASSIGN arrays_list SEM')
    def array_assigns(self, p):
        return "bool {0} {1} = {2} ;".format(p.NAME,p.arrays,p.arrays_list)
    #--------------------------------
    @_('IF condition THEN in_statements END SEM')
    def if_stmt(self, p):
        return str("if({0}){{{1}}}".format(p.condition,p.in_statements))
    
    @_('IF condition THEN in_statements ELSE in_statements END SEM')
    def if_stmt(self, p):
        return str("if({0}){{{1}}}else {{{2}}}".format(p.condition,p.in_statements0,p.in_statements1))
    #--------------------------------
    @_('FOR name TO expr DO in_statements END SEM')
    def loop_stmt(self, p):
        return str("for({0};{1} <= {2};{3}++){{{4}}}".format(p.name,p.name,p.expr,p.name,p.in_statements))
    @_('FOR name DOWNTO expr DO in_statements END SEM')
    def loop_stmt(self, p):
        return str("for({0};{1} >= {2};{3}--){{{4}}}".format(p.name,p.name,p.expr,p.name,p.in_statements))
    @_('WHILE condition DO in_statements END SEM')
    def loop_stmt(self, p):
        return str("while({0}){{{1}}}".format(p.condition,p.in_statements))
    #-------------------------------
    @_('CCODE STRING SEM')
    def ccode(self, p):
        return "{0}".format(p.STRING)
    #-------------------------------
    @_('NAME LPAREN params_call RPAREN')
    def call_func(self, p):
        return "{0}({1})".format(p.NAME,p.params_call)
    @_('NAME LPAREN RPAREN')
    def call_func(self, p):
        return "{0}()".format(p.NAME)
    @_('PRINT LPAREN params_call RPAREN')
    def call_func(self, p):
        return "printf({0}) ".format(p.params_call)
    #-------------------------------
    @_('STRUCT NAME struct_var_assigns END SEM')
    def struct_assign(self, p):
        return "\nstruct {0} {{{1}}};\n".format(p.NAME,p.struct_var_assigns)
    @_('struct_var_assign')
    def struct_var_assigns(self, p):
        return "{0}\n".format(p.struct_var_assign)
    @_('struct_var_assigns struct_var_assign')
    def struct_var_assigns(self, p):
        return "{0}\n{1}".format(p.struct_var_assigns,p.struct_var_assign) 
    @_('INTVAR NAME SEM')
    def struct_var_assign(self, p):
        return "\nint {0} ;".format(p.NAME)        
    @_('STRINGVAR NAME SEM')
    def struct_var_assign(self, p):
        return "\nstring {0};".format(p.NAME)
    @_('CHARVAR NAME SEM')
    def struct_var_assign(self, p):
        return "\nchar {0} ;".format(p.NAME)
    @_('BOOLVAR NAME SEM')
    def struct_var_assign(self, p):
        return "\nbool {0} ;".format(p.NAME)
    @_('NAME NAME SEM')
    def struct_var_assign(self, p):
        return "\n{0}* {1} ;".format(p.NAME0,p.NAME1)
    @_('const_assign')
    def struct_var_assign(self, p):
        return "\n{0}".format(p.const_assign)
    
