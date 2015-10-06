import numpy as np
import matplotlib.pyplot as plt

def __fitness_vs_generation(data, fun, options = {}):

    # Create a sub-plot for each problem.
    problems = data.groupby('problem')
    fig, axes = plt.subplots(nrows=int(np.ceil(len(problems)/3.0)),
                             ncols=3,
                             figsize=(16,8))
    for i, (name, sub) in enumerate(problems):
        sx, sy = i / 3, i % 3
        sub = sub.groupby('generation')
        sub = sub.apply(lambda g: g.groupby('seed')['fitness'].aggregate(fun))
        sp = sub.plot(kind='line', legend=False, ax=axes[sx, sy])
        sp.set_xlabel('Generation')
        sp.set_ylabel('Fitness (score)')
        axes[sx, sy].set_title(name)

    # Minimise overlap and add space for the super-title.
    plt.suptitle(options['title'], fontsize=20)
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)

    return fig

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

    # Create a sub-plot for each problem.
    problems = data.groupby('problem')
    fig, axes = plt.subplots(nrows=int(np.ceil(len(problems)/3.0)),
                             ncols=3,
                             figsize=(16,8))
    for i, (name, sub) in enumerate(problems):
        sx, sy = i / 3, i % 3
        sub = sub.groupby('seed')
        sub = sub.apply(lambda g: g.groupby('generation')['fitness'].max().cummax())
        sub = sub.transpose()
        sp = sub.plot(kind='line', legend=False, ax=axes[sx, sy])
        sp.set_xlabel('Generation')
        sp.set_ylabel('Fitness (score)')
        axes[sx, sy].set_title(name)

    # Minimise overlap and add space for the super-title.
    plt.suptitle(options.get('title', 'Fitness of best solution at each generation'),
                 fontsize=20)
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)

    return fig
