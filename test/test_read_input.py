
import os
import tempfile
import pytest
import yaml
from src.read_input import ReadInput

# Helper function to create a temporary YAML file
def create_temp_yaml(data):
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file.write(data)
        return temp_file.name

# Test cases
def test_read_input_file_found():
    # Create a temporary YAML file
    yaml_data = """
    key1: value1
    key2: value2
    """
    yaml_file = create_temp_yaml(yaml_data)

    # Instantiate ReadInput class
    reader = ReadInput(os.path.basename(yaml_file))

    # Check if the dictionary contains the expected data
    assert reader.dict == {'key1': 'value1', 'key2': 'value2'}

def test_read_input_file_not_found():
    # Instantiate ReadInput class with a non-existent file
    with pytest.raises(FileNotFoundError) as e:
        ReadInput("nonexistent.yaml")

    # Assert that the specific exception type is raised
    assert isinstance(e.value, FileNotFoundError)


def test_read_input_invalid_yaml():
    # Create a temporary YAML file with invalid YAML syntax
    invalid_yaml_data = "key: value\nkey2: value2:invalid"
    yaml_file = create_temp_yaml(invalid_yaml_data)

    # Instantiate ReadInput class
    with pytest.raises(yaml.YAMLError) as e:
        ReadInput(os.path.basename(yaml_file))

    # Assert that the specific exception type is raised
    assert isinstance(e.value, yaml.YAMLError)
