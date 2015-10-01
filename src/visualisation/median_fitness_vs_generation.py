import numpy as np
import storage
from line_graph import LineGraph

class MedianFitnessVsGeneration(LineGraph):

    def prepare(self, data):
        ds = data.group_by('generation').project("fitness")\
                .transform(lambda d: np.median(d))
        return zip(*ds.pairs())

    def draw(self, options = {}):
        options['title'] = options.get('title', 'Median Fitness vs. Generation')
        options['x'] = options.get('x', 'Generation')
        options['y'] = options.get('y', 'Median Fitness')
        super(MedianFitnessVsGeneration, self).draw(options)

# Register this visualisation.
storage.register("median_fitness_vs_generation", MedianFitnessVsGeneration)
