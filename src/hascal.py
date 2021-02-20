
#--------------------------------------------------------------
# | Hascal Programming Language --- Hascal Compiler v1.2.4     |
# | Copyright (c) 2019-2021 Hascal Development Team            |
# --------------------------------------------------------------

from os import execv, system, getenv, path, listdir
from sys import argv
import sys
from subprocess import DEVNULL, STDOUT, check_call
from h_parser import Parser
from h_lexer import Lexer
from h_error import HascalException
from core.colorama import init, Fore
from pathlib import Path

class HascalExecutor():
    def __init__(self, filename, lexer, parser):
        # the name of the file
        self.filename = self.__get_file_name(filename)

        self.lexical_analyser = lexer
        self.token_parser = parser

        # the (.d) output file
        self.dlang_output_filename = self.__get_dlang_filename(self.filename)

        self.execute_hascal_script()


    def __get_file_name(self, filename):
        if not filename.endswith(".has"):
            has_source_error = HascalException(
                "The specified file is not a hascal(.has) file",
                "UnsupportedExtension"
            )
            sys.exit()
        
        return filename

    # get the django filename
    def __get_dlang_filename(self, filename):
        filename = path.basename(filename).split(".")[0]
        return f"{filename}.d"

    # the main execution process
    def execute_hascal_script(self):
        file_content = self.read_file(self.filename)
        parsed_content = self.token_parser.parse(
            self.lexical_analyser.tokenize(file_content)
        )

        self.__create_dlang_source()

    # read the file
    def read_file(self, filename):
        if path.exists(filename):
            with open(filename, "r") as file_reader:
                return str(file_reader.read())
        else:
            file_not_found = HascalException(
                f"{filename} not found",
                "FileNotFound"
            )

    def __create_dlang_source(self):
        temp = self.token_parser.src_imports
        self.token_parser.src_imports = "\nimport std.stdio;\n" + temp

        with open(self.dlang_output_filename, "w") as dlang_writer:
            dlang_writer.write(
                self.token_parser.src_imports + self.token_parser.src_before_main +
                self.token_parser.src_all + self.token_parser.src_main +
                self.token_parser.src_end
            )
        try:
            check_call(
                ['dmd', self.dlang_output_filename, '-of=' + argv[1][:-4]] ,stdout=DEVNULL,stderr=STDOUT
            )
        except:
            exception = HascalException(
                "Your code has an error",
                "UnknownException"
            )

 

# Main
if __name__ == '__main__':
    init()

    # create a new lexer
    lexer = Lexer()

    # create a new parser
    parser = Parser()
    version = "1.2.4"
    if len(argv) == 1:
        print(f"Hascal Compiler v{version} {sys.platform} ")
        print(
            "Copyright (c) 2019-2021 Hascal Development Team,\nAll rights reserved.\n"
        )
        print("usage : hascal <inputfile.has>")
        print("enter following command for show help :\n\thascal --help")
    elif argv[1] == "help" or argv[1] == "-h" or argv[1] == "--help":
        print(
            f"Hascal Compiler v{version} {sys.platform}\nCopyright (c) 2019-2021 Hascal Development Team,\nAll rights reserved.\n"
        )
        print(
            "Enter following command in terminal to build a hascal file :\nhascal <inputfile.has>"
        )
        print("\nother commands :")
        print("\t--help , -h , help : show help")
        print("\t--version , -v , version : show compiler version")
    elif argv[1] == "version" or argv[1] == "-v" or argv[1] == "--version":
        print(f"Hascal Compiler v{version} {sys.platform} ")
        print(
            "Copyright (c) 2019-2021 Hascal Development Team,\nAll rights reserved."
        )
    else:
        # if sys.platform.startswith('win32'):
        #     if argv[1].endswith(".has"):
        #         output_d = "tmp.d"
        #         try:
        #             with open(argv[1], "r") as fin:
        #                 parser.parse(lexer.tokenize(fin.read()))
        #         except FileExistsError:
        #             print(
        #                 Fore.RED +
        #                 f"Hascal : Cannot found {argv[1]}\nHascal : No such file or directory"
        #             )

        #         with open(output_d, "w") as fout:
        #             temp = parser.src_imports
        #             parser.src_imports = "\nimport std.stdio;\n" + temp
        #             fout.write(parser.src_imports + parser.src_before_main +
        #                        parser.src_all + parser.src_main +
        #                        parser.src_end)

        #         try:
        #             tmp0 = argv[1]
        #             tmp = '-of=' + tmp0[:-4]
        #             check_call(['dmd', output_d, tmp],
        #                        stdout=DEVNULL,
        #                        stderr=STDOUT)
        #         except:
        #             print(Fore.RED + "Hascal : Your code has error", end=' ')
        #     else:
        #         print(Fore.RED + "Hascal : Please add \".has\" to your file",
        #               end=' ')
        hascal_executor = HascalExecutor(
            argv[1],
            lexer,
            parser
        )
       