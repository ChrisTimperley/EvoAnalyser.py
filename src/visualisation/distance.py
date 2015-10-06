import numpy as np
import matplotlib.pyplot as plt

def __distance_to_origin_vs_generation(data, fun, options = {}):
    problems = data.groupby('problem')
    n = len(problems)

    # Create a sub-plot for each problem.
    fig, axes = plt.subplots(nrows=int(np.ceil(len(problems)/3.0)),
                             ncols=3,
                             figsize=(16,8))

    # Create a sub-plot for each problem.
    #fig, axes = plt.subplots(nrows=int(np.ceil(len(problems)/3.0)), ncols=3)
    for i, (name, sub) in enumerate(problems):
        sx, sy = i / 3, i % 3
        sub = sub.groupby('generation')
        sub = sub.apply(lambda g: g.groupby('seed')['distance_to_origin'].aggregate(fun))
        sp = sub.plot(kind='line', legend=False, ax=axes[sx, sy])
        sp.set_xlabel('Generation')
        sp.set_ylabel('Distance (num. statements changed)')
        axes[sx, sy].set_title(name)

    # Minimise overlap and add space for the super-title.
    plt.suptitle(options['title'], fontsize=20)
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)

    return fig

"""
Constructs a line graph showing the mean distance from each individual within
the population to the origin at a given generation, for a collection of random
seeds, for each problem.
"""
def mean_distance_to_origin_vs_generation(data, options = {}):
    options['title'] = options.get('title', 'Mean distance to original program at each generation')
    options['y'] = options.get('y', 'Mean distance to original program (statements changed)')
    return __distance_to_origin_vs_generation(data, np.mean, options)

"""
Constructs a line graph showing the median distance from each individual within
the population to the origin at a given generation, for a collection of random
seeds, for each problem.
"""
def median_distance_to_origin_vs_generation(data, options = {}):
    options['title'] = options.get('title', 'Median distance to original program at each generation')
    options['y'] = options.get('y', 'Median distance to original program (statements changed)')
    return __distance_to_origin_vs_generation(data, np.median, options)

"""
Constructs a line graph showing the maximum distance from each individual within
the population to the origin at a given generation, for a collection of random
seeds, for each problem.
"""
def max_distance_to_origin_vs_generation(data, options = {}):
    options['title'] = options.get('title', 'Max. distance to original program at each generation')
    options['y'] = options.get('y', 'Max. distance to original program (statements changed)')
    return __distance_to_origin_vs_generation(data, np.max, options)

"""
Constructs a line graph showing the minimum distance from each individual within
the population to the origin at a given generation, for a collection of random
seeds, for each problem.
"""
def min_distance_to_origin_vs_generation(data, options = {}):
    options['title'] = options.get('title', 'Min. distance to original program at each generation')
    options['y'] = options.get('y', 'Min. distance to original program (statements changed)')
    return __distance_to_origin_vs_generation(data, np.min, options)
