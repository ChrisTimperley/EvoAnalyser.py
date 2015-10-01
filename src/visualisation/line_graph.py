from visualisation import Visualisation
import matplotlib.pyplot as plt

class LineGraph(Visualisation):

    def __init__(self, data):
       self.line = self.prepare(data) 

    def draw(self):
        plt.figure()
        plt.plot(self.line[0], self.line[1]) 
        plt.title('I NEED A TITLE')
        plt.xlabel('X LABEL')
        plt.ylabel('Y LABEL')
        plt.grid(True)

        # And optionally, some axis.
        #plt.axis([0, num_generations, 0.0, 1.0])

        plt.show()
