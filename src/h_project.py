import os as os
import json as Json
from lol.prompt import Prompt
from h_error import HascalException
from core.colorama import Fore, init


def throw_success_message(message):
    print(Fore.GREEN + f"SUCCESS:{message}")


class Project():
    def __init__(self):
        self.project_information = self.get_project_info()

        init()

        self.directory = self.create_project_directory(
            self.project_information["project-name"])
        self.create_config_file()

        self.create_all_directories(self.directory)

    def create_all_directories(self, directory):
        create_folders = [
            os.path.join(directory, "src"),
            os.path.join(directory, "test")
        ]

        for folder in create_folders:
            os.mkdir(folder)

        create_files = [
            os.path.join(directory, "src", "main.has"),
            os.path.join(directory, "test", "test.has")
        ]

        for index, filename in enumerate(create_files):
            self.write_to_file(filename, f"# {filename}")

            throw_success_message(f"[{index}] Created {filename}")

    def write_to_file(self, filename, file_content):
        with open(filename, "w") as file_writer:
            file_writer.write(file_content)

    def create_config_file(self):
        self.write_to_file(os.path.join(self.directory, "hascal.json"),
                           Json.dumps(self.project_information, indent=6))

        throw_success_message("Created config file")

    # get the project details
    def get_project_info(self):
        parameters = [
            {
                "value": "Project Name"
            },
            {
                "value": "Description"
            },
            {
                "value": "Author"
            },
        ]

        project_info_solutions = {}

        for parameter_query in parameters:
            prompt = Prompt(parameter_query["value"]).prompt()

            project_info_solutions[parameter_query["value"].lower().replace(
                " ", "-")] = str(prompt)

        return project_info_solutions

    def create_project_directory(self, project_name):
        if project_name == ".":
            project_dir = os.getcwd()
        else:
            project_dir = os.path.join(os.getcwd(), project_name)

        if os.path.exists(project_dir):
            if project_dir == os.getcwd():
                if len(os.listdir(project_dir)) is not 0:
                    exception = HascalException("Folder is not empty",
                                                "FolderNotEmpty")
                return project_dir
            else:
                exception = HascalException("File or Folder already exists",
                                            "FileOrFolderExists")
        else:
            os.mkdir(project_dir)
            return project_dir
