from .h_lexer import Lexer
from .h_parser import Parser
from .h_compiler import Generator
from .h_help import *
from os.path import isfile
from subprocess import DEVNULL, STDOUT, check_call
import sys
from .colorama import init,Fore
import os
class HascalCompiler(object):
    def __init__(self,argv):
        init() # init colorama

        self.code = ""
        self.lexer = Lexer()
        self.parser = Parser()
        self.generator = Generator()
        self.argv = argv
        
        # arguments checking
        if len(self.argv) > 1 :
            if self.argv[1] == "-h" or self.argv[1] == "--help":
                # show help
                output_message = [f"Hascal Compiler {HASCAL_COMPILER_VERSION} {sys.platform}",
                                    "Copyright (c) 2019-2021 Hascal Development Team,",
                                    "All rights reserved.",
                                    "\nEnter following command for compile a Hascal program :",
                                    "hascal <inputfile.has>",
                                    "other commands:",
                                    "\t--help,-h : show help",
                                    "\t--version,-v : show version"]
                for msg in output_message:
                    print(msg)
                sys.exit()
            elif self.argv[1] == "-v" or self.argv[1] == "--version":
                # show version
                print(f"Hascal {HASCAL_COMPILER_VERSION} {sys.platform}")
            else :
                if not self.argv[1].endswith(".has"):
                    # show file extension error 
                    print(f"Error : The specified file is not a hascal(.has) file")
                else :
                    try:
                        with open(argv[1]) as fin:
                            self.code = fin.read()
                        self.compile()
                    except FileNotFoundError :
                        print("Error : File not found")
        else:
            output_message = [f"Hascal Compiler {HASCAL_COMPILER_VERSION} {sys.platform}",
                                "Copyright (c) 2019-2021 Hascal Development Team,",
                                "All rights reserved.",
                                "\nEnter following command for compile a Hascal program :",
                                "hascal <inputfile.has>",
                                "other commands:",
                                "\t--help,-h : show help",
                                "\t--version,-v : show version"]
            for msg in output_message:
                print(msg)
            sys.exit()

    def compile(self):
        tokens = self.lexer.tokenize(self.code)
        tree = self.parser.parse(tokens)
        output = self.generator.generate(tree)
        outname = self.argv[2] if len(self.argv) > 2 else "com.d"

        # write output d code in a file
        with open(outname, 'w') as fout:
            fout.write(output)

        # set output excutable file
        tmp0 = self.argv[1]
        tmp = '-of=' + tmp0[:-4]

        # compile with dmd compiler
        try :
            check_call(['dmd',"com.d", tmp],stdout=DEVNULL,stderr=STDOUT)
            os.remove("com.d")
        except :
            output_messages = [
                "Error : Your code have error(s)",
                "Check these items :",
                "\t1-incompatible types",
                "\t2-functions arguements and types and length of arguments",
                "\t3-modify consts",
                "\tand more..."
                "\nif you could not troubleshooting your code , create an issue in hascal github repository(github.com/hascal/hascal) ,we helps you "
            ]
            for msg in output_messages:
                print(Fore.RED+msg)
        