import os
import yaml
import logging

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
        self.working_dir = os.path.dirname(os.path.abspath(__file__))
        self.dict: dict = self.yaml_to_dict(self._join_path())

    def _join_path(self):
        """Joins the working directory with the file name
        Returns:
            str: Path to the input file
        """
        try:
            file_path = os.path.join(self.working_dir, self.file_name)
            if os.path.exists(file_path):
                logging.info(f"{self.file_name}: File found")
                return file_path
            else:
                raise FileNotFoundError(f"{self.file_name}: File not found")
        except Exception as e:
            logging.error(f"Error while joining path: {e}")
            raise

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
            logging.error(f"Error while reading YAML file: File not found - {yaml_path}")
            raise
        except Exception as e:
            logging.error(f"Error while reading YAML file: {e}")
            raise




