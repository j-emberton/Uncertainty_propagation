import pydoe as doe
import pandas as pd
from scipy.stats.distributions import norm

class LHS:
    def __init__(self, data: dict, samples: int = 1000, criterion: str = 'maximin', iterations: int = 1000, random_state: int = None):
        self.data = data
        self.dimensions = None
        self.samples = samples
        self.criterion = criterion
        self.iterations = iterations
        self.random_state = random_state
        self.sample_dataframe = self._parse_input_dict()

    def _parse_input_dict(self):
        column_names = self._get_dimension_names()
        self.dimensions = len(column_names)
        means, std_devs = self._extract_mean_std_dev(self.data, column_names)
        df = self._gen_LHS(means, std_devs, column_names)
        return df
    
    def _get_dimension_names(self):
        dimension_names = list(self.data.keys())
        return dimension_names
    
    def _extract_mean_std_dev(self, data: dict, column_names: list):
        means = {}
        std_devs = {}

        for n in column_names:
            first_level_dict = data[n]
            means[n] = first_level_dict['mean']
            std_devs[n] = first_level_dict['std_dev']

        return means, std_devs
    
    def _gen_LHS(self, means: dict, std_devs: dict, column_names: list):
        design = doe.lhs(self.dimensions, samples=self.samples, criterion=self.criterion, iterations=self.iterations, random_state=self.random_state)

        for i in range(self.dimensions):
            design[:, i] = norm(loc=means[column_names[i]], scale=std_devs[column_names[i]]).ppf(design[:, i])

        df = pd.DataFrame(design, columns=column_names)
        
        return df
