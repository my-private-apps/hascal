# -------------------------------------------------
# | Newlla Framework v1.0 - HaCross Compiler v1.4 |
# -------------------------------------------------

from os import execl
from sys import argv
from h_parser import Parser
from h_lexer import Lexer
# Main 
if __name__ == '__main__':
    lexer = Lexer()
    parser = Parser()
      
    if len(argv) == 1 :
      print("Hascal Compiler : No such file or directory")
    elif argv[1] == "help" :
      print("Hascal Compiler v1.2\nCopyright (c) 2019-2020 Hascal Development Team.\nAll rights reserved.\n")
      print("Enter following command in terminal to build a hascal file :\nhascal <filename>")
    else :       
        with open(argv[1], "r") as fin:           
            parser.parse(lexer.tokenize(fin.read()))
            with open("tmp.c","w") as fout:
                fout.write(parser.src_imports +parser.src_before_main+ parser.src_all + parser.src_main + parser.src_end)
        #a = ["tmp.c"]
        #execl("tcc.exe","tmp.c")           
        
