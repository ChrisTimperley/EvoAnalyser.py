import numpy as np
import storage
from visualisation import Visualisation

class MeanFitnessVsGeneration(Visualisation):

    def draw(self, data, options = {}):
        
        # Generate the data frame for this graph.
        data = data.groupby('generation')
        data = data.apply(lambda g: g.groupby('seed').aggregate(np.mean)['fitness'])
        
        # Plot this graph. 
        plot = data.plot(kind='line', legend=False)
        plot.set_ylabel(options.get('y', 'Mean Fitness'))
        plot.set_xlabel(options.get('x', 'Generation'))
        plot.set_title(options.get('title', 'Mean Fitness vs. Generation'))

        return plot

# Register this visualisation.
storage.register("mean_fitness_vs_generation", MeanFitnessVsGeneration)
