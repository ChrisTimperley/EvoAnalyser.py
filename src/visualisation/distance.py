import numpy as np
import matplotlib.pyplot as plt

def __distance_to_origin_vs_generation(data, fun, options = {}):
    problems = data.groupby('problem')

    # Create a sub-plot for each problem.
    fig, axes = plt.subplots(nrows=int(np.ceil(len(problems)/3.0)), ncols=3)

    # Create a sub-plot for each problem.
    #fig, axes = plt.subplots(nrows=int(np.ceil(len(problems)/3.0)), ncols=3)
    for i, (name, sub) in enumerate(problems):

        # Calculate sub-plot co-ordinates.
        sx = i / 3
        sy = i % 3
        
        sub = sub.groupby('generation')
        sub = sub.apply(lambda g: g.groupby('seed')['distance_to_origin'].aggregate(fun))
        # Plot the line for each seed.
        #plt.subplot(2, sx + 1, sy + 1)
        #plt.plot()
        print sx, sy
        sub.plot(kind='line', legend=False, ax=axes[sx, sy])

    return None

    """
    # Let's do this for multiple problems...
    data = data.groupby('problem').apply(lambda g: \
        g.groupby('generation').apply(lambda g: g.groupby('seed')['distance_to_origin'].aggregate(fun)) \
    )
    data = data.transpose().unstack().reset_index()
    data.columns = ['problem', 'generation', 'seed', 'distance']
    data = data.groupby('problem')
    num_problems = len(data)

    print "problems: %d" % num_problems

    # Create a sub-plot for each problem.
    fig, axes = plt.subplots(nrows=int(np.ceil(num_problems/3.0)), ncols=3)

    for i, (name, sub) in enumerate(data):

        print sub.groupby('seed')

        sx = int(np.ceil(i/3.0))
        sy = i % 3
        plot = sub.plot(kind='line', x='generation', y='distance', legend=False, ax=axes[sx, sy])
        axes[sx, sy].set_title(name)

    #plot.set_ylabel(options['y'])
    #plot.set_xlabel(options.get('x', 'Generation'))
    #plot.set_title(options['title'])
    return plot
    """

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
