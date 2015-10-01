import numpy as np
import storage
from line_graph import LineGraph

# MultiLineGraph
# BoxPlot

class MeanFitnessVsGeneration(LineGraph):

    def prepare(self, data):
        ds = data.group_by('generation').project("fitness")\
                .transform(lambda d: np.mean(d))
        return zip(*ds.pairs())

    def draw(self, options = {}):
        options['title'] = options.get('title', 'Mean Fitness vs. Generation')
        options['x'] = options.get('x', 'Generation')
        options['y'] = options.get('y', 'Mean Fitness')
        
        # Generate the axis for the graph.
        #gens = len(self.line[0])

        # Ideally we could do with knowing the problem that this data set
        # belongs to.

        super(MeanFitnessVsGeneration, self).draw(options)

# Register this visualisation.
storage.register("mean_fitness_vs_generation", MeanFitnessVsGeneration)
