# --------------------------------------------------------------
# | Hascal Programming Language --- Hascal Compiler v1.2.4     |
# | Copyright (c) 2019-2021 Hascal Development Team            |
# --------------------------------------------------------------

from os import execv
from os import system
from os import getenv
from sys import argv
import sys
from subprocess import DEVNULL,STDOUT,check_call
from h_parser import Parser
from h_lexer import Lexer
from core.colorama import init, Fore
from pathlib import Path
# Main 
if __name__ == '__main__':
    init()
    lexer = Lexer()
    parser = Parser()
    version = "1.2.4"
    if len(argv) == 1 :
        print(Fore.GREEN + "Hascal Compiler : No such file or directory")
        print(Fore.GREEN + "usage : hascal <inputfile.has>")
    elif argv[1] == "help" :
        print("Hascal Compiler v1.2.0\nCopyright (c) 2019-2021 Hascal Development Team.\nAll rights reserved.\n")
        print("Enter following command in terminal to build a hascal file :\nhascal <inputfile.has>")
    elif argv[1] == "version":
        print(f"Hascal version : hascal {version} {sys.platform}")
    else :
        if sys.platform.startswith('win32'):
            if argv[1].endswith("has"):
                input_output = "{0}".format(argv[1])
                input_output = input_output[:-3]
                input_output += "d"
                input_output = getenv('HPATH') + "\\cache\\" + input_output
                try :
                    with open(argv[1], "r") as fin:           
                        parser.parse(lexer.tokenize(fin.read()))
                except FileExistsError:
                    print(Fore.RED+f"Hascal : Cannot found {argv[1]}\nHascal : No such file or directory")

                with open(input_output,"w") as fout:
                    temp = parser.src_imports
                    parser.src_imports = "\nimport std.stdio;\n" + temp
                    fout.write(parser.src_imports +parser.src_before_main+ parser.src_all + parser.src_main + parser.src_end)
                output_file = argv[1]
                output_file_name =  ""

                try :
                    check_call(['dmd',input_output],stdout=DEVNULL,stderr=STDOUT)
                except:
                    print(Fore.RED + "Hascal : Your code has error",end=' ')
        elif sys.platform.startswith('linux'):
            if argv[1].endswith("has"):
                input_output = "{0}".format(argv[1])
                input_output = input_output[:-3]
                input_output += "d"
                input_output = getenv('HPATH') + "/cache/" + input_output 
                try :
                    with open(argv[1], "r") as fin:           
                        parser.parse(lexer.tokenize(fin.read()))
                except FileExistsError:
                    print(Fore.RED+f"Hascal : Cannot found {argv[1]}\nHascal : No such file or directory")
                
                with open(input_output,"w") as fout:
                    temp = parser.src_imports
                    parser.src_imports = "\nimport std.stdio;\n" + temp
                    fout.write(parser.src_imports +parser.src_before_main+ parser.src_all + parser.src_main + parser.src_end)
                output_file = argv[1]
                output_file_name =  ""

                try :
                    check_call(['dmd',input_output],stdout=DEVNULL,stderr=STDOUT)
                except:
                    print(Fore.RED + "Hascal : Your code has error",end=' ')
