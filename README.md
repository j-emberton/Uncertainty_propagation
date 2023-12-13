# Uncertainty Propagation

## Description

This project is intended to provide a facility to assess the impact of input uncertainty on analysis outputs via latin hypercube sampling.

Underlying principles:
    - define input variables and their statistical characteristics in an input yaml file \n
    - use these definitions to generate a random latin hypercube sampling scheme with samples weighted by equal area under CDF \n
    - run each sample from the LHS dataset and collate results
    - collate and regress statistical description onto output variables
    - test output data for confidence level of mean values

Work to date:
    - Repo setup based on own project template
        - provides basic project architecture with initial definition of pre-committ hooks and linting, github actions to run unit tests, structure to allow future packaging for distribution, license, readme and requirements.
    - Define input file read-in functionality and initial associated unit tests
    - Define functionality to generate LHS sampling scheme
    - Define functionality to downselect target solver and provide solver definition

Future tasks:
    - Refine unit tests
    - Complete doctrings for self documentation
    - Add remaining functionality
    - Package and distribute



## Status
Under development. Publicly available for code review only.


## Contributing

If you want to contribute to this project, please contact the author

## License

This project is licensed under the GNU GPL3 terms and conditions
