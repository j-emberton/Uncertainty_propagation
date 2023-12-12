import sys
from .read_input import ReadInput
from .gen_LHS import gen_LHS
from .solver import Solver



def main(input_file):

    data_dict = ReadInput(input_file)

    sample_df = gen_LHS(data_dict)

    solver = Solver(solver_choice)

    columns_to_use = sample_df.columns

    result_df = sample_df.apply(lambda row: solver(*row[columns_to_use], axis=1))

    return sample_df.concat(result_df, axis=1)




if __name__ == '__main__':
    
    if len(sys.argv) == 2:
        file_arg = sys.argv[0]
        solver_choice = sys.argv[1]
        print(f'The input file is {file_arg}')
        print(f'The solver choice is {solver_choice}')
    else:
        print('Incorrect number of arguments. Please provide the input file name and solver choice.')

    result = main(file_arg)