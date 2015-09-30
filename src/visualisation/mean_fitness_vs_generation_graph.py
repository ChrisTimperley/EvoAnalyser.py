import matplotlib.pyplot as plt
from visualisation import Visualisation

class MeanFitnessVsGeneration(Visualisation):
    name = "mean_fitness_vs_generation"

    def prepare(self, data):

        # Need to group data by generation (category vs. number).
        data.group_by("generation") # view("group[generation]")

        # Transform each generation into a sequence of fitness values.
        # view("project[fitness]") -> view("group[generation]; project[fitness]")
        .project("fitness")

        # Reduce each sequence of fitness values to their mean.
        .reduce_to("mean")

    def visualise(self, data):
        plt.figure()
        plt.boxplot(self.prepare(data))
        plt.ylabel('Fitness Score')
        plt.title('Distribution of fitness values for a single run.')
        plt.show()
