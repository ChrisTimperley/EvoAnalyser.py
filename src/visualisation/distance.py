import numpy as np

def mean_distance_to_origin_vs_generation(data, options = {}):
    data = data.groupby('generation')
    data = data.apply(lambda g: g.groupby('seed')['distance_to_origin'].aggregate(np.mean))

    # Plot the data.
    plot = data.plot(kind='line', legend=False)
    plot.set_ylabel(options.get('y', 'Distance to original program (statements changed)'))
    plot.set_xlabel(options.get('x', 'Generations Passed'))
    plot.set_title(options.get('title', 'Distance to original program vs. generations passed'))
    return plot
