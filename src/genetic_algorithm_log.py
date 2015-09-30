class GeneticAlgorithmLog:

    @staticmethod
    def process(log):
        generations = GeneticAlgorithmLog.__parse_generations(log.search)
        return GeneticAlgorithmLog(generations)

    @staticmethod
    def __parse_generations(search):
        generations = [[]]
        gen = generations[0]
        g = 0
        for ind in search:

            # Determine if this individual starts the beginning of a new
            # generation.
            if ind.pop('generation') > g:
                gen = []
                generations.append(gen)
                g += 1

            # Process this individual.
    
            # Add this individual to the current generation.
            gen.append(ind)

        return generations

    @staticmethod
    def __parse_setup():
        pass

    @staticmethod
    def __parse_problem():
        pass

    def __init__(self, generations):
        self.generations = generations

    # Returns the number of individuals encountered during this run, where
    # revisits are counted equally.
    def num_visited():
        return reduce(lambda sm, g: sm + len(g), self.generations)

    # Returns the number of generations (including initialisation) performed
    # during this run.
    def num_generations():
        return len(self.generations)
