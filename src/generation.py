import re
from patch import Patch
from individual import Individual
from population import Population

# Holds information about a given generation from an EA run.
class Generation:
    
    @staticmethod
    def from_string(problem, s):
        lines = s.split("\n")

        # Extract the generation number.
        gen = re.match("Generation (\d+)", lines[1])
        assert gen != None
        gen = int(gen.group(1))

        # Strip out all the excess lines and reform the definition.
        lines = lines[3:-1]
        s = '\n'.join(lines)

        # Split the generation info into each of its sub-sections.
        subsections = s.split('-' * 80)[1:]

        # Selection
        s = subsections.pop(0)
        selection = map(lambda ln: int(ln.split('; ')[1]), s.split('\n')[3:-1])

        # Crossover
        s = subsections.pop(0)
        crossover = map(lambda ln: ln.split('; ')[1:], s.split('\n')[3:-1])
        crossover = map(lambda ln: [map(int, ln[0].split(', ')), Patch.from_string(ln[1])], crossover)

        # Mutation
        s = subsections.pop(0)
        mutation = map(lambda ln: ln.split('; ')[1], s.split('\n')[3:-1])
        mutation = map(Patch.from_string, mutation)

        # Evaluation
        s = subsections.pop(0)
        evaluation = map(lambda ln: ln.split('; ')[1], s.split('\n')[3:-1])
        evaluation = map(float, evaluation)

        # Build and return the information object
        return Generation(problem, selection, crossover, mutation, evaluation)

    # Constructs a generation info object from information about a given
    # generation.
    def __init__(self, problem, selection, crossover, mutation, evaluation):
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation
        self.evaluation = evaluation

        # Construct the offspring for this generation.
        self.offspring = []
        for i in range(len(self.evaluation)):
            self.offspring.append(Individual(problem,
                                             i,
                                             self.crossover[i][0],
                                             self.mutation[i],
                                             self.evaluation[i]))
        self.offspring = Population(self.offspring)

    def offspring_to_string(self, problem):
        s = []
        for i, ind in enumerate(self.offspring):
            s.append(ind.to_string(distance_to_origin=self.distance_to_origin[i],
                                   lines=ind.patch.to_lines(problem)))
        return '\n'.join(s)


