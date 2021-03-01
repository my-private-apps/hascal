<<<<<<< HEAD
#--------------------------------------------------------------
# | Hascal Programming Language --- Hascal Compiler v1.2.4     |
# | Copyright (c) 2019-2021 Hascal Development Team            |
# --------------------------------------------------------------

# from os import execv, system, getenv, path, listdir, system, mkdir
from os import (
    execv,
    system,
    getenv,
    path,
    listdir,
    mkdir,
    getcwd
)
import platform as platform
from sys import argv
import sys
from subprocess import DEVNULL, STDOUT, check_call
from h_parser import Parser
from h_lexer import Lexer
from h_error import HascalException
from h_project import Project
from core.colorama import init, Fore
from pathlib import Path

HASCAL_COMPILER_VERSION = '1.2.4'


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
                "UnsupportedExtension")
            sys.exit()

        return filename

    # get the django filename
    def __get_dlang_filename(self, filename):
        filename = path.basename(filename).split(".")[0]
        if "build" not in listdir(getcwd()):
            mkdir("build")
        return path.join("build", f"{filename}.d")

    # the main execution process
    def execute_hascal_script(self):
        file_content = self.read_file(self.filename)
        parsed_content = self.token_parser.parse(
            self.lexical_analyser.tokenize(file_content))

        self.__create_dlang_source()

    # read the file
    def read_file(self, filename):
        if path.exists(filename):
            with open(filename, "r") as file_reader:
                return str(file_reader.read())
        else:
            file_not_found = HascalException(f"{filename} not found",
                                             "FileNotFound")
            sys.exit()

    def __create_dlang_source(self):
        temp = self.token_parser.src_imports
        self.token_parser.src_imports = "\nimport std.stdio;\n" + temp

        with open(self.dlang_output_filename, "w") as dlang_writer:
            dlang_writer.write(self.token_parser.src_imports +
                               self.token_parser.src_before_main +
                               self.token_parser.src_all +
                               self.token_parser.src_main +
                               self.token_parser.src_end)
        try:
            # check_call(
            #     ['dmd', self.dlang_output_filename, '-of=' + argv[1][:-4]],
            #     stdout=DEVNULL,
            #     stderr=STDOUT)
            check_call(
                [
                    "dmd",
                    f"{self.dlang_output_filename}",
                    f"-of={path.join('build', 'dist', 'main')}"
                ]
            )
        except:
            exception = HascalException("Your code has an error",
                                        "UnknownException")

class HascalArgumentParser(object):
    def __init__(self, command_line_argument):
        self.arguments = command_line_argument[1:]

        self.compiler_version = "1.2.4"

        self.lexer = Lexer()
        self.parser = Parser()

        self.parser_arguments(self.arguments)

    # parse the arguments
    def parser_arguments(self, arguments):
        if len(arguments) == 0:
            self.hascal_compiler()
        else:
            if arguments[0] == "-v" or arguments[0] == "--version":
                print(
                    f"Hascal Compiler {self.compiler_version} on {sys.platform}"
                )
                print(
                    "Copyright (c) 2019-2021 Hascal Development Team,\nAll rights reserved."
                )
            elif arguments[0] == "-h" or arguments[0] == "--help":
                self.show_help_message()

            elif arguments[0] == "init":
                project = Project()
            else:
                hascal_file_executor = HascalExecutor(arguments[0], self.lexer,
                                                      self.parser)

    # hascal compiler details
    def hascal_compiler(self):
        console_output_texts = [
            f"Hascal Compiler {self.compiler_version} on {sys.platform}",
            "Copyright (c) 2019-2021 Hascal Development Team,\nAll rights reserved.\n",
            "usage : hascal <inputfile.has>"
            "enter following command for show help :\n\thascal --help"
        ]
        for output_text in console_output_texts:
            print(output_text)

    # show help message
    def show_help_message(self):
        console_output_texts = [
            f"Hascal Compiler {self.compiler_version} on {sys.platform}\nCopyright (c) 2019-2021 Hascal Development Team,\nAll rights reserved.\n"
            "Enter following command in terminal to build a hascal file :\nhascal <inputfile.has>"
            "\nother commands :", "\t--help , -h , help : show help",
            "\t--version , -v , version : show compiler version"
        ]
        for output_text in console_output_texts:
            print(output_text)


if __name__ == "__main__":
    hascal_argument_parser = HascalArgumentParser(argv)
=======
#!/usr/bin/env python3
from sys import argv 
from core.h_builder import HascalCompiler
if __name__ == "__main__":    
      HascalCompiler(argv)
            

      
      
      
>>>>>>> upstream/main
