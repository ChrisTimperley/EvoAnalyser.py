import numpy as np
from visualisation import Visualisation

class MeanDistanceToOriginVsGeneration(Visualisation):
    def draw(self, data, options = {}):
        data = data.groupby('generation')
        data = data.apply(lambda g: g.groupby('seed').aggregate(np.mean)['distance_to_origin'])
        plot = data.plot(kind='line', legend=False)
        plot.set_ylabel(options.get('y', 'Mean Distance to Origin'))
        plot.set_xlabel(options.get('x', 'Generation'))
        plot.set_title(options.get('title', 'Mean Distance to Origin vs. Generation'))
        return plot
