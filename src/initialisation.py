from patch import Patch
from population import Population
from individual import Individual

# Holds information about the initialisation phase of a given EA run.
class Initialisation:
    
    # Constructs an initialisation information object from a given string
    # definition (sourced from a log file).
    @staticmethod
    def from_string(problem, s):
        lines = s.split('\n')

        assert lines[1] == 'Initialisation'

        # Parse each individual definition (id, genome, fitness).
        lines = lines[3:-1]
        genomes, fitnesses = zip(*map(lambda ln: ln.split('; ')[1:], lines))
        genomes = map(Patch.from_string, genomes)
        fitnesses = map(float, fitnesses)
        pop = map(lambda (i, (g, f)): Individual(problem, i, [], g, f),
                  enumerate(zip(genomes, fitnesses)))
        pop = Population(pop)

        return Initialisation(pop)

    # Constructs a new initialisation information object from a given initial
    # population.
    def __init__(self, population):
        self.population = population
