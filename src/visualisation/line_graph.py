from visualisation import Visualisation
import matplotlib.pyplot as plt

class LineGraph(Visualisation):

    def __init__(self, data):
       self.line = self.prepare(data) 

    def draw(self, options = {}):
        plt.figure()
        plt.plot(self.line[0], self.line[1]) 
        plt.title(options.get('title', 'Untitled Line Graph'))
        plt.xlabel(options.get('x', 'Unlabelled X Axis'))
        plt.ylabel(options.get('y', 'Unlabelled Y Axis'))
        plt.grid(True)

        # And optionally, some axis.
        if options.has_key('axis'):
            plt.axis(options['axis'])

        plt.show()