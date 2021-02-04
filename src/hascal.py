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
        print(f"Hascal Compiler v{version} {sys.platform} ")
        print("Copyright (c) 2019-2021 Hascal Development Team,\nAll rights reserved.\n")
        print("usage : hascal <inputfile.has>")
        print("enter following command for show help :\n\thascal --help")
    elif argv[1] == "help" or argv[1] == "-h" or argv[1] == "--help":
        print(f"Hascal Compiler v{version} {sys.platform}\nCopyright (c) 2019-2021 Hascal Development Team,\nAll rights reserved.\n")
        print("Enter following command in terminal to build a hascal file :\nhascal <inputfile.has>")
        print("\nother commands :")
        print("\t--help , -h , help : show help")
        print("\t--version , -v , version : show compiler version")
    elif argv[1] == "version" or argv[1] == "-v" or argv[1] == "--version":
        print(f"Hascal Compiler v{version} {sys.platform} ")
        print("Copyright (c) 2019-2021 Hascal Development Team,\nAll rights reserved.")
    else :
        if sys.platform.startswith('win32'):
            if argv[1].endswith(".has"):
                output_d = "tmp.d"
                try :
                    with open(argv[1], "r") as fin:           
                        parser.parse(lexer.tokenize(fin.read()))
                except FileExistsError:
                    print(Fore.RED+f"Hascal : Cannot found {argv[1]}\nHascal : No such file or directory")

                with open(output_d,"w") as fout:
                    temp = parser.src_imports
                    parser.src_imports = "\nimport std.stdio;\n" + temp
                    fout.write(parser.src_imports +parser.src_before_main+ parser.src_all + parser.src_main + parser.src_end)

                try :
                    tmp0 = argv[1]
                    tmp = '-of='+tmp0[:-4]
                    check_call(['dmd',output_d,tmp],stdout=DEVNULL,stderr=STDOUT)
                except:
                    print(Fore.RED + "Hascal : Your code has error",end=' ')
            else:
                print(Fore.RED + "Hascal : Please add \".has\" to your file",end=' ')
        elif sys.platform.startswith('linux'):
            if argv[1].endswith(".has"):
                output_d = "tmp.d"
                try :
                    with open(argv[1], "r") as fin:           
                        parser.parse(lexer.tokenize(fin.read()))
                except FileExistsError:
                    print(Fore.RED+f"Hascal : Cannot found {argv[1]}\nHascal : No such file or directory")
                
                with open(output_d,"w") as fout:
                    temp = parser.src_imports
                    parser.src_imports = "\nimport std.stdio;\n" + temp
                    fout.write(parser.src_imports +parser.src_before_main+ parser.src_all + parser.src_main + parser.src_end)
                try :
                    tmp0 = argv[1]
                    tmp = '-of='+tmp0[:-4]
                    check_call(['dmd',output_d,tmp],stdout=DEVNULL,stderr=STDOUT)
                except:
                    print(Fore.RED + "Hascal : Your code has error",end=' ')
