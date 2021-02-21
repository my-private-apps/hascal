import os as os
import json as Json
from lol.prompt import Prompt
from h_error import HascalException

class Project():
    def __init__(self):
        self.project_information = self.get_project_info()

        self.directory = self.create_project_directory(self.project_information["project-name"])


    # get the project details
    def get_project_info(self):
        parameters = [
            {"value":"Project Name"},
            {"value":"Description"},
            {"value":"Author"},
        ]

        project_info_solutions = {}

        for parameter_query in parameters:
            prompt = Prompt(parameter_query["value"]).prompt()
            
            project_info_solutions[
                parameter_query["value"].lower().replace(
                    " ", "-"
                )
            ] = str(prompt)

        return project_info_solutions

    def create_project_directory(self, project_name):
        if project_name == ".":
            project_dir = os.getcwd()
        else:
            project_dir = os.path.join(os.getcwd(), project_name)
        
        if os.path.exists(project_dir):
            if project_dir == os.getcwd():
                if len(os.listdir(project_dir)) is not 0:
                    exception = HascalException(
                        "Folder is not empty",
                        "FolderNotEmpty"
                    )
                return project_dir
            else:
                exception = HascalException(
                    "File or Folder already exists",
                    "FileOrFolderExists"
                )
        else:
            os.mkdir(project_dir)
            return project_dir

