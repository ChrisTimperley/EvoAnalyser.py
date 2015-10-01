import numpy as np
from line_graph import LineGraph

# LineGraph
# MultiLineGraph
# BoxPlot

class MeanFitnessVsGeneration(LineGraph):
    name = "mean_fitness_vs_generation"

    def prepare(self, data):
        ds = data.group_by('generation').project("fitness")\
                .transform(lambda d: np.mean(d))
        return zip(*ds.pairs())
