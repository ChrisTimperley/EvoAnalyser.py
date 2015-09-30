class GeneticAlgorithmLog:

    @staticmethod
    def process(log):
        generations = __parse_generations(log.search)
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
