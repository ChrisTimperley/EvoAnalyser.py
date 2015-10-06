import numpy as np
from visualisation import Visualisation

class MeanFitnessVsGeneration(Visualisation):
    def draw(self, data, options = {}):
        data = data.groupby('generation')
        data = data.apply(lambda g: g.groupby('seed').aggregate(np.mean)['fitness'])
        
        plot = data.plot(kind='line', legend=False)
        plot.set_ylabel(options.get('y', 'Mean Fitness'))
        plot.set_xlabel(options.get('x', 'Generation'))
        plot.set_title(options.get('title', 'Mean Fitness vs. Generation'))
        return plot
