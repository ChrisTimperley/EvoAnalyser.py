import matplotlib.pyplot as plt
from visualisation import Visualisation

# Fitness boxplot.
# (view: fitness)
# (type: boxplot)

class FitnessBoxPlot(Visualisation):
    name = "fitness_box_plot"

    # Requires that there is a fitness property and that it is, or can be
    # mapped to a scalar value.
    def prepare(self, data):
        return map(lambda p: p.fitness, data)

    def visualise(self, data):
        plt.figure()
        plt.boxplot(self.prepare(data))
        plt.ylabel('Fitness Score')
        plt.title('Distribution of fitness values for a single run.')
        plt.show()
