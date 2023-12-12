import os
import yaml


class ReadInput:

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.working_dir = os.getcwd()
        self.dict: dict = self.yaml_to_dict(self._join_path())

    def _join_path(self):

        return os.path.join(self.working_dir, self.file_name)

    def yaml_to_dict(self, yaml_path):
        with open(yaml_path, 'r') as yaml_file:
        # Load YAML data into a Python dictionary
            yaml_data = yaml.safe_load(yaml_file)
        return yaml_data
    

    



