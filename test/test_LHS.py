import pytest
import pandas as pd
from src.gen_LHS import LHS


# Set up data for testing
data = {
    'dimension1': {'mean': 0, 'std_dev': 1},
    'dimension2': {'mean': 5, 'std_dev': 2},
    'dimension3': {'mean': -3, 'std_dev': 0.5}
}
samples = 1000
criterion = 'maximin'

# Initialize LHS object
lhs = LHS(data, samples, criterion, iterations, random_state)

# Test parsing the input dictionary
def test_parse_input_dict():
    assert isinstance(lhs.sample_dataframe, pd.DataFrame)

# Test getting dimension names
def test_get_dimension_names():
    expected_dimensions = ['dimension1', 'dimension2', 'dimension3']
    assert lhs._get_dimension_names() == expected_dimensions

# Test extracting means and std_devs
def test_extract_mean_std_dev():
    expected_means = {'dimension1': 0, 'dimension2': 5, 'dimension3': -3}
    expected_std_devs = {'dimension1': 1, 'dimension2': 2, 'dimension3': 0.5}
    means, std_devs = lhs._extract_mean_std_dev(['dimension1', 'dimension2', 'dimension3'])
    assert means == expected_means
    assert std_devs == expected_std_devs

# Test generating LHS
def test_gen_LHS():
    df = lhs._gen_LHS(
        {'dimension1': 0, 'dimension2': 5, 'dimension3': -3},
        {'dimension1': 1, 'dimension2': 2, 'dimension3': 0.5},
        ['dimension1', 'dimension2', 'dimension3']
    )
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (samples, len(data))

# Test invalid criterion
def test_invalid_criterion():
    with pytest.raises(ValueError, match="Invalid criterion. Please choose a valid criterion."):
        LHS(data, samples, criterion='invalid_criterion')