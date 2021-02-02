from h_lexer import Lexer
from core.sly import Parser

from os import getenv
import sys
class Parser(Parser):
    tokens = Lexer.tokens
    #src_imports =  "typedef char* string;\n#include<stdbool.h>\n#include<string.h>\n"
    src_imports = "" #"import std.stdio;\n"
    src_before_main = "\n\n"
    src_all = "\nint main(string[] args){\n "
    src_main = " "
    src_end =  "\nreturn 0;}"
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
        return str(p.in_statement)
    @_('in_statements in_statements')
    def in_statements(self, p):
        return str(p.in_statements0 + p.in_statements1)
    @_('in_statements')
    def in_statements(self, p):
        return str(p.in_statements)
    
    #----------------------------------
    
    # function <name> {
    #   <in_statements>
    # }
    
    # or:
    
    # function <name>() {
    #   <in_statements>
    # }
    
    # or:
    
    # function <name>(<params>) {
    #   <in_statements>
    # }
    
    # or:
    
    # function <name> as <return_type> {
    #   <in_statements>
    # }
    
    # or:

    # function <name>() as <return_type> {
    #   <in_statements>
    # }
    
    # or:
    
    # function <name>(<params>) as <return_type> {
    #   <in_statements>
    # }
    @_('func_declare')
    def statement(self, p):
        self.src_before_main += "\n{0}\n".format(p.func_declare)
    #----------------------------------
    # use "<lib_name>";
    @_('USE STRING SEM')
    def statement(self, p):
        if sys.platform.startswith('win32'):
            tmp = p.STRING
            path = tmp.split('.')
            final_path = str(getenv('HPATH') + "\\hlib"+"\\")
            
            ends_of_path = path[-1]
            for x in path[:-1]:
                final_path += x + "\\"
            final_path += ends_of_path + ".has"

            try :
                with open(final_path, 'r') as f:
                    parser = Parser()
                    parser.parse(Lexer().tokenize(f.read()))
                    self.src_imports += '\n'+parser.src_imports+'\n' + parser.src_main + '\n' + parser.src_before_main + '\n'
            except FileNotFoundError :
                print(f"Hascal : cannot found {p.STRING} library. Are you missing a library ?")
                
        elif sys.platform.startswith('linux'):
            tmp = p.STRING
            path = tmp.split('.')
            final_path = str(getenv('HPATH') + "\\hlib"+"\\")
            
            ends_of_path = path[-1]
            for x in path[:-1]:
                final_path += x + "\\"
            final_path += ends_of_path + ".has"

            try :
                with open(final_path, 'r') as f:
                    parser = Parser()
                    parser.parse(Lexer().tokenize(f.read()))
                    self.src_imports += '\n'+parser.src_imports+'\n' + parser.src_main + '\n' + parser.src_before_main + '\n'
            except FileNotFoundError :
                print(f"Hascal : cannot found {p.STRING} library. Are you missing a library ?")
        
    # local use "<lib_name>";   
    @_('LOCAL USE STRING SEM')
    def statement(self, p):
        replacedValue = str(p.STRING).replace(".", "\\")
        path = r'{0}.has'.format(replacedValue)
        try :
            with open(path, 'r') as f:
                parser = Parser()
                parser.parse(Lexer().tokenize(f.read()))
                self.src_imports += '\n'+parser.src_imports+'\n' + parser.src_before_main + '\n' + parser.src_main + '\n'
        except FileNotFoundError :
            print(f"Hascal : cannot found {replacedValue} library. Are you missing a library ?"+path)
            
    @_('EXT STRING SEM')
    def statement(self, p):
        final_path = p.STRING + ".d"
        try :
            with open(final_path, 'r') as f:
                parser = Parser()
                self.src_imports += '\n'+f.read()+ '\n'
        except FileNotFoundError :
            print(f"Hascal : cannot found {p.STRING} library. Are you missing a library ?")
    @_('LOCAL EXT STRING SEM')
    def statement(self, p):
        tmp = p.STRING
        path = tmp.split('.')
        final_path = str(getenv('HPATH') + "\\hlib"+"\\")
            
        ends_of_path = path[-1]
        for x in path[:-1]:
            final_path += x + "\\"
        final_path += ends_of_path + ".d"
        
        path = r'./hlib/{0}.d'.format(p.STRING)
        try :
            with open(final_path, 'r') as f:
                parser = Parser()
                self.src_imports += '\n'+f.read()+ '\n'
        except FileNotFoundError :
            print(f"Hascal : cannot found {p.STRING} library. Are you missing a library ?")

    #----------------------------------

    # struct <name> {
    #   <vars>
    #   <functions>
    # }
    @_('struct_assign')
    def statement(self, p):
        self.src_before_main += "\n{0}\n".format(p.struct_assign)
    #----------------------------------

    # var <name> : <var_type> ;
    # or:
    # var <name> : <var_type> = <expr> ;
    # or:
    # var <name> = <expr> ;
    @_('var_assign')
    def statement(self, p):
        self.src_main += "\n{0}\n".format(p.var_assign)        
    #----------------------------------
    # const <name> = <expr> ;
    @_('const_assign')
    def statement(self, p):
        self.src_main += "\n{0}\n".format(p.const_assign)
    #----------------------------------

    # if <condition> {
    #   <in_statements>
    # }
    @_('if_stmt')
    def statement(self, p):
        self.src_main += "\n{0}\n".format(p.if_stmt)
    #----------------------------------

    # enum <name> {
    #   <enum_names>
    # }
    @_('enum_declare')
    def statement(self, p):
        self.src_main += "\n{0}\n".format(p.enum_declare)
    #---------------------------------
    # for <name> to <expr> {
    #   <in_statements>
    # }
    
    # or :
    
    # for <name> downto <expr> {
    #   <in_statements>
    # }
    
    # or :
    
    # while <condition> {
    #   <in_statements>
    # }
    @_('loop_stmt')
    def statement(self, p):
        self.src_main += "\n{0}\n".format(p.loop_stmt)
        
    #----------------------------------
    # <name>(<params_call>);
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
    # return <expr> ;
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
    # break;
    # continue ;
    @_('break_loop')
    def in_statement(self, p):
        return "\n{0}\n".format(p.break_loop)
    @_('continue_loop')
    def in_statement(self, p):
        return "\n{0}\n".format(p.continue_loop)
        
    #----------------------------------
    @_('enum_declare')
    def in_statement(self, p):
        return "\n{0}\n".format(p.enum_declare)
    #-----------------------------------
    @_('array_assigns')
    def in_statement(self, p):
        return "\n{0}\n".format(p.array_assigns)
#---------------------------------------------#
#   Expertions                                #
#---------------------------------------------#
    @_('MINUS expr %prec UMINUS')
    def expr(self, p):
        return "-{0}".format(p.expr)    
    @_('name')
    def expr(self, p):
        return str(p.name)

    @_('name LBRACE andis RBRACE')
    def expr(self, p):
        return "{0}{1}".format(p.name,p.andis)
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
        return str('\''+p.CHAR+'\'')
    
    @_('num')
    def expr(self, p):
        return "{0}".format(p.num)
    @_('float')
    def expr(self, p):
        return "{0}".format(p.float)

    @_('expr DOT expr')
    def expr(self, p):
        return "{0}.{1}".format(p.expr0,p.expr1)
    @_('expr PLUS expr')
    def expr(self, p):
        return "{0}+{1}".format(p.expr0,p.expr1)
    @_('expr ALFA expr')
    def expr(self, p):
        return "{0}~{1}".format(p.expr0,p.expr1)
    @_('expr MINUS expr')
    def expr(self, p):
        return "{0}-{1}".format(p.expr0,p.expr1)
    @_('expr TIMES expr')
    def expr(self, p):
        return "{0}*{1}".format(p.expr0,p.expr1)
    @_('expr DIVIDE expr')
    def expr(self, p):
        return "{0}/{1}".format(p.expr0,p.expr1)

    @_('STRING')
    def expr(self, p):
        return str('"'+p.STRING+'"')

    @_('arrays_list')
    def expr(self, p):
        return str(p.arrays_list)

    #@_('LBRACE andis RBRACE')
    #def expr(self, p):
    #    return "{0}".format(p.andis)
    
    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return "({0})".format(p.expr)

    @_('call_func')
    def expr(self, p):
        return "{0}".format(p.call_func)

    #@_('MINUS expr')
    #def expr(self, p):
    #    return str("{0}{1}".format(p.MINUS,p.expr))
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
    @_('expr')
    def condition(self, p):
        return str("{0}".format(p.expr))
    @_('call_func')
    def condition(self, p):
        return str("{0}".format(p.call_func))
    @_('condition')
    def conditions(self, p):
        return str("{0}".format(p.condition))
    @_('conditions AND condition')
    def conditions(self, p):
        return str("{0} && {1}".format(p.conditions,p.condition))
    @_('conditions OR condition')
    def conditions(self, p):
        return str("{0} || {1}".format(p.conditions,p.condition))

    @_('NOT name')
    def condition(self, p):
        return str("!{0}".format(p.name))
#---------------------------------------------#
#   End Conditions                            #
#---------------------------------------------#
    @_('name_t')
    def name(self, p):
        return p.name_t
    
    @_('name DOT name_t')
    def name(self, p):
        return p.name +"."+ p.name_t

    @_('NAME DOT NAME')
    def name_t(self, p):
        return str(p.NAME0+"."+p.NAME1)
    
    @_('NAME')
    def name_t(self, p):
        return str(p.NAME)

    #------------------------------
    @_('num DOT NUMBER')
    def float(self, p):
        return str("{0}.{1}".format(p.num,p.NUMBER))
    #------------------------------
    @_('params_call COMMA param_call')
    def params_call(self, p):
        return str("{0} , {1}".format(p.params_call,p.param_call))
    
    @_('param_call')
    def params_call(self, p):
        return p.param_call

    @_('expr')
    def param_call(self, p):
        return p.expr
    #------------------------------
    @_('param')
    def params(self, p):
        return p.param
    
    @_('params COMMA param')
    def params(self, p):
        return p.params +","+ p.param

    @_('NAME INTVAR')
    def param(self, p):
        return p.INTVAR+" "+ p.NAME
    @_('NAME STRINGVAR ')
    def param(self, p):
        return "string "+ p.NAME
    @_('NAME BOOLVAR ')
    def param(self, p):
        return "bool "+ p.NAME
    @_('NAME CHARVAR ')
    def param(self, p):
        return "char "+ p.NAME
    @_('NAME FLOATVAR ')
    def param(self, p):
        return "float "+ p.NAME
    @_('NAME NAME ')
    def param(self, p):
        return "{0} {1} ".format(p.NAME1,p.NAME0)

    @_('NAME INTVAR LBRACE expr RBRACE')
    def param(self, p):
        return "int ["+p.expr+"] "+ p.NAME
    @_('NAME STRINGVAR LBRACE expr RBRACE')
    def param(self, p):
        return "string ["+p.expr+"] "+ p.NAME
    @_('NAME BOOLVAR LBRACE expr RBRACE ')
    def param(self, p):
        return "bool ["+p.expr+"] "+ p.NAME
    @_('NAME CHARVAR LBRACE expr RBRACE ')
    def param(self, p):
        return "char ["+p.expr+"] "+ p.NAME
    @_('NAME FLOATVAR LBRACE expr RBRACE ')
    def param(self, p):
        return "float ["+p.expr+"] "+ p.NAME
    @_('NAME  NAME LBRACE expr RBRACE')
    def param(self, p):
        return "{0} [{1}] {2}".format(p.NAME1,p.expr,p.NAME0)
    #----------------------------
    @_('TRUE')
    def boolean(self, p):
        return str(p.TRUE)
    @_('FALSE')
    def boolean(self, p):
        return str(p.FALSE)
    #----------------------------
    @_('INTVAR')
    def return_type(self, p):
        return "int"
    @_('STRINGVAR')
    def return_type(self, p):
        return "string"
    @_('CHARVAR')
    def return_type(self, p):
        return "char"
    @_('BOOLVAR')
    def return_type(self, p):
        return "bool"
    @_('FLOATVAR')
    def return_type(self, p):
        return "float"
    @_('NAME')
    def return_type(self, p):
        return "{0}".format(p.NAME)

    @_('INTVAR LBRACE RBRACE')
    def return_type(self, p):
        return "int[]"
    @_('STRINGVAR LBRACE RBRACE')
    def return_type(self, p):
        return "string[]"
    @_('CHARVAR LBRACE RBRACE')
    def return_type(self, p):
        return "char[]"
    @_('BOOLVAR LBRACE RBRACE')
    def return_type(self, p):
        return "bool[]"
    @_('FLOATVAR LBRACE RBRACE')
    def return_type(self, p):
        return "float[]"
    @_('NAME LBRACE RBRACE')
    def return_type(self, p):
        return "{0}[]".format(p.NAME)
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
    @_('LBRACE array_list RBRACE')
    def arrays_list(self, p):
        return "["+p.array_list+"]"
    #@_('LBC array_list COMMA array_list RBC')
    #def arrays_list(self, p):
    #    return "{"+p.array_list0 +','+ p.array_list1+"}"
    
    @_('expr')
    def array_list_t(self, p):
        return str("{0}".format(p.expr))
    @_('array_list_t')
    def array_list(self, p):
        return str("{0}".format(p.array_list_t))
    @_('array_list COMMA array_list_t')
    def array_list(self, p):
        return str("{0},{1}".format(p.array_list,p.array_list_t))
    @_(' ')
    def array(self, p):
        return " "
    @_('expr')
    def array(self, p):
        return str("[{0}]".format(p.expr))
    @_('array')
    def arrays(self, p):
        return str("{0}".format(p.array))
    #--------------------------------
    @_('VAR NAME DOTDOT INTVAR SEM')
    def var_assign(self, p):
        return "int {0} ;".format(p.NAME)
    @_('VAR NAME DOTDOT INTVAR ASSIGN expr SEM')
    def var_assign(self, p):
        return "int {0} = {1};".format(p.NAME,p.expr)
    
    @_('VAR NAME ASSIGN expr SEM')
    def var_assign(self, p):
        return "auto {0} = {1};".format(p.NAME,p.expr)
    
    @_('VAR NAME DOTDOT STRINGVAR SEM')
    def var_assign(self, p):
        return "string {0} ;".format(p.NAME)
    @_('VAR NAME DOTDOT STRINGVAR ASSIGN expr SEM')
    def var_assign(self, p):
        return "string {0} = {1} ;".format(p.NAME,p.expr)
    
    @_('VAR NAME DOTDOT CHARVAR SEM')
    def var_assign(self, p):
        return "char {0};".format(p.NAME)
    @_('VAR NAME DOTDOT CHARVAR ASSIGN CHAR SEM')
    def var_assign(self, p):
        return "char {0} = {1};".format(p.NAME,p.CHAR)
    
    @_('VAR NAME DOTDOT BOOLVAR SEM')
    def var_assign(self, p):
        return "bool {0};".format(p.NAME)
    @_('VAR NAME DOTDOT BOOLVAR ASSIGN boolean SEM')
    def var_assign(self, p):
        return "bool {0} = {1};".format(p.NAME,p.boolean)
    
    @_('VAR NAME DOTDOT NAME SEM')
    def var_assign(self, p):
        return  str("{0} {1};".format(p.NAME1,p.NAME0))
    @_('VAR NAME DOTDOT NAME LPAREN params_call RPAREN SEM')
    def var_assign(self, p):
        return  str("{0} {1} = {{{2}}};".format(p.NAME1,p.NAME0,p.params_call))
    
    @_('VAR NAME ASSIGN NEW name SEM')
    def var_assign(self, p):
        return  str("{0} {1};".format(p.name,p.NAME))    
    @_('VAR NAME ASSIGN NEW NAME LPAREN params_call RPAREN SEM')
    def var_assign(self, p):
        return  str("{0} {1} = {{{2}}};".format(p.NAME1,p.NAME0,p.params_call))
    
    @_('VAR NAME DOTDOT FLOATVAR SEM')
    def var_assign(self, p):
        return "float {0};".format(p.NAME)
    @_('VAR NAME DOTDOT FLOATVAR ASSIGN expr SEM')
    def var_assign(self, p):
        return "float {0} = {1};".format(p.NAME,p.expr)
    
    @_('expr ASSIGN expr SEM')
    def var_assign(self, p):
        return str("{0} = {1};".format(p.expr0,p.expr1))
    @_('expr ASSIGN NEW name  SEM')
    def var_assign(self, p):
        return str("{0} = {1}();".format(p.expr,p.name))
    @_('expr ASSIGN NEW NAME LPAREN params_call RPAREN SEM')
    def var_assign(self, p):
        return  str("{0} = {1}({2});".format(p.expr,p.NAME,p.params_call))
    #--------------------------------
    @_('CONST NAME ASSIGN expr SEM')
    def const_assign(self, p):
        return "const {0} = {1} ;".format(p.NAME,p.expr)
    
    @_('CONST NAME AS STRINGVAR ASSIGN expr SEM')
    def const_assign(self, p):
        return "const string {0} = {1} ;".format(p.NAME,p.expr)
    @_('CONST NAME AS CHARVAR ASSIGN expr SEM')
    def const_assign(self, p):
        return "const char {0} = {1} ;".format(p.NAME,p.expr)
    @_('CONST NAME AS BOOLVAR ASSIGN boolean SEM')
    def const_assign(self, p):
        return "const bool {0} = {1} ;".format(p.NAME,p.boolean)
    
    @_('CONST NAME AS FLOATVAR ASSIGN expr SEM')
    def const_assign(self, p):
        return "const float {0} = {1} ;".format(p.NAME,p.expr)

    @_('CONST NAME AS INTVAR ASSIGN expr SEM')
    def const_assign(self, p):
        return "const int {0} = {1} ;".format(p.NAME,p.expr)
    
    @_('CONST NAME DOTDOT NAME ASSIGN arrays_list SEM')
    def const_assign(self, p):
        return "const {0} {1} = {{{2}}} ;".format(p.NAME1,p.NAME0,p.arrays_list)
    #--------------------------------
    @_('BREAK SEM')
    def break_loop(self, p):
        return "break;"
    #--------------------------------
    @_('CONTINUE SEM')
    def continue_loop(self, p):
        return "continue;"
    #--------------------------------
    @_('VAR NAME DOTDOT INTVAR LBRACE arrays RBRACE ASSIGN arrays_list SEM')
    def array_assigns(self, p):
        return "int {0} {1} = {2} ;".format(p.arrays,p.NAME,p.arrays_list)

    @_('VAR NAME DOTDOT FLOATVAR LBRACE arrays RBRACE ASSIGN arrays_list SEM')
    def array_assigns(self, p):
        return "float {0} {1} = {2} ;".format(p.arrays,p.NAME,p.arrays_list)
    
    @_('VAR NAME DOTDOT STRINGVAR LBRACE arrays RBRACE ASSIGN arrays_list SEM')
    def array_assigns(self, p):
        return "string {0} {1} = {2};".format(p.arrays,p.NAME,p.arrays_list)
    
    @_('VAR NAME DOTDOT BOOLVAR LBRACE arrays RBRACE ASSIGN arrays_list SEM')
    def array_assigns(self, p):
        return "bool {0} {1} = {2};".format(p.arrays,p.NAME,p.arrays_list)
    
    @_('VAR NAME DOTDOT name LBRACE arrays RBRACE ASSIGN arrays_list SEM')
    def array_assigns(self, p):
        return "{0} {1} {2} = {3} ;".format(p.name,p.arrays,p.NAME,p.arrays_list)
    
    @_('VAR NAME DOTDOT INTVAR LBRACE arrays RBRACE SEM')
    def array_assigns(self, p):
        return "int {0} {1} ;".format(p.arrays,p.NAME)

    @_('VAR NAME DOTDOT STRINGVAR LBRACE arrays RBRACE SEM')
    def array_assigns(self, p):
        return "string {0} {1} ;".format(p.arrays,p.NAME)

    @_('VAR NAME DOTDOT FLOATVAR LBRACE arrays RBRACE SEM')
    def array_assigns(self, p):
        return "float {0} {1} ;".format(p.arrays,p.NAME)
    
    @_('VAR NAME DOTDOT BOOLVAR LBRACE arrays RBRACE SEM')
    def array_assigns(self, p):
        return "bool {0} {1} ;".format(p.arrays,p.NAME,p.arrays_list)
    
    @_('VAR NAME DOTDOT name LBRACE arrays RBRACE SEM')
    def array_assigns(self, p):
        return "{0} {1} {2} ;".format(p.name,p.arrays,p.NAME)
    #--------------------------------
    @_('IF conditions LBC in_statements RBC')
    def if_stmt(self, p):
        return str("if({0}){{{1}}}".format(p.conditions,p.in_statements))
    
    @_('IF conditions LBC in_statements RBC ELSE LBC in_statements RBC')
    def if_stmt(self, p):
        return str("if({0}){{{1}}}else {{{2}}}".format(p.conditions,p.in_statements0,p.in_statements1))

    @_('IF conditions LBC in_statements RBC ELSE if_stmt')
    def if_stmt(self, p):
        return str("if({0}){{{1}}}else {2}".format(p.conditions,p.in_statements,p.if_stmt))
    #--------------------------------
    @_('FOR name ASSIGN expr TO expr  LBC in_statements RBC')
    def loop_stmt(self, p):
        return str("for({0}={1};{2} <= {3};{4}++){{{5}}}".format(p.name,p.expr0,p.name,p.expr1,p.name,p.in_statements))
    @_('FOR name ASSIGN expr DOWNTO expr LBC in_statements RBC')
    def loop_stmt(self, p):
        return str("for({0}={1};{2} >= {3};{4}--){{{5}}}".format(p.name,p.expr0,p.name,p.expr1,p.name,p.in_statements))
    @_('WHILE conditions LBC in_statements RBC')
    def loop_stmt(self, p):
        return str("while({0}){{{1}}}".format(p.conditions,p.in_statements))
    #-------------------------------
    @_('name LPAREN params_call RPAREN')
    def call_func(self, p):
        return "{0}({1})".format(p.name,p.params_call)
    @_('name LPAREN RPAREN')
    def call_func(self, p):
        return "{0}()".format(p.name)
    @_('PRINT LPAREN params_call RPAREN')
    def call_func(self, p):
        return "writeln({0})".format(p.params_call)
    #-------------------------------
    
    @_('STRUCT NAME LBC struct_declares RBC')
    def struct_assign(self, p):
        return "\nstruct {0} {{{1}}}\n".format(p.NAME,p.struct_declares)
    
    @_('struct_declare')
    def struct_declares(self, p):
        return "\n{0}\n".format(p.struct_declare)
    @_('struct_declares struct_declare')
    def struct_declares(self, p):
        return "{0}\n{1}".format(p.struct_declares,p.struct_declare)
    
    @_('VAR NAME DOTDOT INTVAR  SEM')
    def struct_declare(self, p):
        return "\nint {0} ;".format(p.NAME)        
    @_('VAR NAME DOTDOT STRINGVAR SEM')
    def struct_declare(self, p):
        return "\nstring {0};".format(p.NAME)
    @_('VAR NAME DOTDOT CHARVAR SEM')
    def struct_declare(self, p):
        return "\nchar {0} ;".format(p.NAME)
    @_('VAR NAME DOTDOT BOOLVAR  SEM')
    def struct_declare(self, p):
        return "\nbool {0} ;".format(p.NAME)
    @_('VAR NAME DOTDOT FLOATVAR  SEM')
    def struct_declare(self, p):
        return "\nfloat {0} ;".format(p.NAME)
    @_('VAR NAME DOTDOT NAME SEM')
    def struct_declare(self, p):
        return "\n{0} {1} ;".format(p.NAME1,p.NAME0)
    @_('const_assign')
    def struct_declare(self, p):
        return "\n{0}".format(p.const_assign)
    @_('func_declare')
    def struct_declare(self, p):
        return "\n{0}\n".format(p.func_declare)
    @_('array_assigns')
    def struct_declare(self, p):
        return "\n{0}\n".format(p.array_assigns)
    #--------------------------------
    @_('FUNCTION NAME LPAREN RPAREN LBC in_statements RBC')
    def func_declare(self, p):
        return "void {0} () {{{1}}}\n".format(p.NAME,p.in_statements)
    @_('FUNCTION NAME LBC in_statements RBC')
    def func_declare(self, p):
        return "void {0} () {{{1}}}\n".format(p.NAME,p.in_statements)
    
    @_('FUNCTION NAME LPAREN params RPAREN LBC in_statements RBC')
    def func_declare(self, p):
        return "\nvoid {0} ({1}) {{{2}}}\n".format(p.NAME,p.params,p.in_statements)

    @_('FUNCTION NAME LPAREN RPAREN  AS return_type LBC in_statements RBC')
    def func_declare(self, p):
        return "\n{0} {1} () {{{2}}}\n".format(p.return_type,p.NAME,p.in_statements)
    @_('FUNCTION NAME AS return_type LBC in_statements RBC')
    def func_declare(self, p):
        return "\n{0} {1} () {{{2}}}\n".format(p.return_type,p.NAME,p.in_statements)

    @_('FUNCTION NAME LPAREN params RPAREN  AS return_type LBC  in_statements RBC')
    def func_declare(self, p):
        return "{0} {1} ({2}) {{{3}}}".format(p.return_type,p.NAME,p.params,p.in_statements)
    #--------------------------------
    @_('ENUM NAME LBC enum_names RBC')
    def enum_declare(self, p):
        return "\nenum {0} {{{1}}}\n".format(p.NAME,p.enum_names)
    @_('enum_name')
    def enum_names(self, p):
        return "\n{0}\n".format(p.enum_name)
    @_('enum_names COMMA enum_name')
    def enum_names(self, p):
        return "\n{0},{1}\n".format(p.enum_names,p.enum_name)
    @_('NAME')
    def enum_name(self, p):
        return "\n{0}\n".format(p.NAME)
