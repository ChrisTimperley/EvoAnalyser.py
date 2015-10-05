import numpy as np
import storage
from visualisation import Visualisation

class NumSolutionsVsProblem(Visualisation):
    def draw(self, data, options = {}):
        data = data.groupby('problem')['ideal'].sum()
        plot = data.plot(kind='bar')
        plot.set_xlabel(options.get('x', 'Problem'))
        plot.set_ylabel(options.get('y', 'No. Solutions Found'))
        plot.set_title(options.get('title', 'Number of solutions found for each problem'))
        return plot

# Register this visualisation.
storage.register('num_solutions_vs_problem',
                 NumSolutionsVsProblem)
