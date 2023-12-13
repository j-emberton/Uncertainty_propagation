import pyDOE as doe
import pandas as pd
from scipy.stats.distributions import norm

class LHS:
    """Generates a Latin Hypercube Sample (LHS) from a dictionary of means and standard deviations."""

    def __init__(self, data: dict, samples: int = 1000, criterion: str = 'maximin', iterations: int = 1000, random_state: int = None):
        """
        Args:
            data (dict): Dictionary of means and standard deviations for each dimension.
            samples (int, optional): Number of samples to generate. Defaults to 1000.
            criterion (str, optional): Criterion to use for generating the LHS. Defaults to 'maximin'.
            iterations (int, optional): Number of iterations to use for generating the LHS. Defaults to 1000.
            random_state (int, optional): Random state to use for generating the LHS. Defaults to None.
            
            """
        self.data = data
        self.dimensions = None
        self.samples = samples
        self.criterion = criterion
        self.iterations = iterations
        self.random_state = random_state
        self.sample_dataframe = self._parse_input_dict()

    def _parse_input_dict(self):
        """Parses the input dictionary and generates a LHS."""
        column_names = self._get_dimension_names()
        self.dimensions = len(column_names)
        means, std_devs = self._extract_mean_std_dev(column_names)
        df = self._gen_LHS(means, std_devs, column_names)
        return df
    
    def _get_dimension_names(self):
        """Gets the names of the dimensions from the input dictionary."""
        dimension_names = list(self.data.keys())
        return dimension_names
    
    def _extract_mean_std_dev(self, column_names: list):
        """Extracts the means and standard deviations from the input dictionary.
            
            Args:
                column_names (list): List of dimension names.
                
                Returns:
                    means (dict): Dictionary of means for each dimension.
                    std_devs (dict): Dictionary of standard deviations for each dimension."""
        means = {}
        std_devs = {}

        for n in column_names:
            first_level_dict = self.data[n]
            means[n] = first_level_dict['mean']
            std_devs[n] = first_level_dict['std_dev']

        return means, std_devs
    
    def _gen_LHS(self, means: dict, std_devs: dict, column_names: list):
        """Generates a LHS from the means and standard deviations.
        
            Args:
                means (dict): Dictionary of means for each dimension.
                std_devs (dict): Dictionary of standard deviations for each dimension.
                column_names (list): List of dimension names.
                
                Returns:
                    df (pd.DataFrame): DataFrame containing the LHS."""
        design = doe.lhs(self.dimensions, samples=self.samples, criterion=self.criterion, iterations=self.iterations, random_state=self.random_state)

        for i in range(self.dimensions):
            design[:, i] = norm(loc=means[column_names[i]], scale=std_devs[column_names[i]]).ppf(design[:, i])

        df = pd.DataFrame(design, columns=column_names)
        
        return df
