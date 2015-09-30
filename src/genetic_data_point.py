import json

class GeneticDataPoint(DataPoint):

    # Constructs a data point for a genetic algorithm from an entry in the log
    # file.
    def __init__(self, data):
        self.position = data['position']
        self.generation = data['generation']
        self.parents = data['parents'] # optional
