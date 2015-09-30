class BestFitnessAnalysis(Analysis):

    name = "best_fitness"

    def compute(data):
        fitnesses = filter(lambda p: p.fitness, data)

        # Assume highest scalar value is best for now.
        return max(fitnesses)
