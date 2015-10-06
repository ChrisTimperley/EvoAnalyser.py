import numpy as np

def __distance_to_origin_vs_generation(data, fun, options = {}):
    data = data.groupby('generation')
    data = data.apply(lambda g: g.groupby('seed')['distance_to_origin'].aggregate(fun))

    # Plot the data.
    plot = data.plot(kind='line', legend=False)
    plot.set_ylabel(options['y'])
    plot.set_xlabel(options.get('x', 'Generation'))
    plot.set_title(options['title'])
    return plot

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
