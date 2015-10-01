import matplotlib.pyplot as plt
from visualisation import Visualisation

class MeanFitnessVsGeneration(Visualisation):
    name = "mean_fitness_vs_generation"

    def prepare(self, data):

        # Need to group data by generation (category vs. number).
        return data.group_by('generation').project("fitness")
            map(lambda g: g.project("fitness").reduce("mean")).\
            items()

    def visualise(self, data):
        plt.figure()
        plt.boxplot(self.prepare(data))
        plt.ylabel('Fitness Score')
        plt.title('Distribution of fitness values for a single run.')
        plt.show()
