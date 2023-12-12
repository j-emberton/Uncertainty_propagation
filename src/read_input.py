import os
import yaml


class ReadInput:
    """Reads the input file and returns a dictionary with the data
    Args:   
        file_name (str): Name of the input file
        Returns:
            dict: Dictionary with the data from the input file
                
    """

    def __init__(self, file_name: str):
        """Constructor method
        Args:
            file_name (str): Name of the input file
        """
        self.file_name = file_name
        self.working_dir = os.getcwd()
        self.dict: dict = self.yaml_to_dict(self._join_path())

    def _join_path(self):
        """Joins the working directory with the file name
        Returns:
            str: Path to the input file
        """
        try:
            return os.path.exists(os.path.join(self.working_dir, self.file_name))
            print(f"{self.file_name}: - File found")

        except FileNotFoundError:
            print("File not found")

    def yaml_to_dict(self, yaml_path):
        """Converts YAML file to a Python dictionary
        
        Args:
            yaml_path (str): Path to the YAML file
            Returns:
                dict: Dictionary with the data from the YAML file
        """
        try:
            with open(yaml_path, 'r') as yaml_file:
            # Load YAML data into a Python dictionary
                yaml_data = yaml.safe_load(yaml_file)
            return yaml_data
        except FileNotFoundError:
            print("File not readable")
    

    



