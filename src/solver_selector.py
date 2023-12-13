

class SolverSelector:
    def __init__(self, solver_name):
        self.solver_name = solver_name
        self.supported_solvers = ['TypeA']
        self.target = self._get_method()

    def _get_method(self):

        if self.solver_name == 'TypeA':
            from src.solvers.TypeA import TypeA
            return TypeA()
        else:
            raise ValueError('Unsupported solver: {}'.format(self.solver_name))
        
    def get_target(self,**kwargs):

        result = self.target(**kwargs)
        
        return result

    