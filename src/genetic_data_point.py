import json
import representation

from data_point import DataPoint

# Represents a single point within the search process of a genetic algorithm.
class GeneticDataPoint(DataPoint):

    # Constructs a data point for a genetic algorithm from an entry in the log
    # file.
    def __init__(self, data):
        self.position = data['position']
        self.generation = data['generation']
        self.parents = data.get('parents', None)

        # Parse the genome according to the genotype used by the algorithm.
        self.genome = representation.Patch.load(data['genome'])

        # Parse the fitness according to the fitness scheme used by the
        # algorithm.
        self.fitness = data['fitness']
