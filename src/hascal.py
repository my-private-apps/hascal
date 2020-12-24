# -------------------------------------------------
# | Hascal Programming Language --- Compiler v1.2 |
# | Copyright 2019-2020 Hascal Development Team   | 
# -------------------------------------------------

from os import execv
from os import system
from sys import argv
import sys
from hascal.h_parser import Parser
from hascal.h_lexer import Lexer
# Main 
if __name__ == '__main__':
    lexer = Lexer()
    parser = Parser()
    version = "1.2.4"
    if len(argv) == 1 :
        print("Hascal Compiler : No such file or directory")
        print("usage : hascal <inputfile.has> <output_file>")
    elif argv[1] == "help" :
        print("Hascal Compiler v1.2\nCopyright (c) 2019-2020 Hascal Development Team.\nAll rights reserved.\n")
        print("Enter following command in terminal to build a hascal file :\nhascal <filename>")
    elif argv[1] == "version":
        print(f"Hascal version : hascal v1.2.4 {sys.platform}")
    else :       
        with open(argv[1], "r") as fin:           
            parser.parse(lexer.tokenize(fin.read()))
                
            with open("tmp.c","w") as fout:
                fout.write(parser.src_imports +parser.src_before_main+ parser.src_all + parser.src_main + parser.src_end)
            output_file = argv[1]
            output_file_name =  ""

            if sys.platform.startswith('linux'):
                output_file_name = output_file[:-3]
                system(f"tcc tmp.c -o {output_file_name}")
            elif sys.platform.startswith('win32'):
                output_file_name = output_file[:-3] + "exe"
                system(f"tcc tmp.c -o {output_file_name}")
        
