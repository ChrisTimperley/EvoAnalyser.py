import numpy as np

def __fitness_vs_generation(data, fun, options = {}):
    data = data.groupby('generation')
    data = data.apply(lambda g: g.groupby('seed')['fitness'].aggregate(fun))

    # Plot the data.
    plot = data.plot(kind='line', legend=False)
    plot.set_ylabel(options['y'])
    plot.set_xlabel(options.get('x', 'Generation'))
    plot.set_title(options['title'])
    return plot

"""
Constructs a line graph showing the best fitness amongst the individuals within
the population at a given generation. Each seed for the problem is given its own
line.
"""
def pbest_fitness_vs_generation(data, options = {}):
    options['title'] = options.get('title', 'Population Best Fitness vs. Generation')
    options['y'] = options.get('y', 'Population Best Fitness')
    return __fitness_vs_generation(data, np.max, options)

"""
Constructs a line graph showing the mean fitness of the individuals within the
population at a given generation. Each seed for the problem is given its own
line.
"""
def mean_fitness_vs_generation(data, options = {}):
    options['title'] = options.get('title', 'Mean Fitness of Population vs. Generation')
    options['y'] = options.get('y', 'Mean Fitness of Population')
    return __fitness_vs_generation(data, np.mean, options)

"""
Constructs a line graph showing the median fitness of the individuals within the
population at a given generation. Each seed for the problem is given its own
line.
"""
def median_fitness_vs_generation(data, options = {}):
    options['title'] = options.get('title', 'Median Fitness of Population vs. Generation')
    options['y'] = options.get('y', 'Median Fitness of Population')
    return __fitness_vs_generation(data, np.median, options)

"""
Constructs a line graph showing the fitness of the best solution found so far
during the search against the current generation. Each seed for the problem is
given its own line.
"""
def best_fitness_vs_generation(data, options = {}):
    data = data.groupby('seed')
    data = data.apply(lambda g: g.groupby('generation')['fitness'].max().cummax())
    data = data.transpose()

    # Plot the data.
    plot = data.plot(kind='line', legend=True)
    plot.set_ylabel(options.get('y', 'Fitness of Best Solution'))
    plot.set_xlabel(options.get('x', 'Generation'))
    plot.set_title(options.get('title', 'Fitness of Best Solution vs. Generation'))

    return plot
