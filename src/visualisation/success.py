import numpy as np

def success_rate_vs_generation(data, options = {}):
   
    # Transform success to cumulative success.

    # Success vs. Generation (per-seed).
    data = data.groupby('seed')
    data = data.apply(lambda g: g.groupby('generation')['ideal'].max().cummax().map(np.float) )
    data = data.apply(np.mean)

    # Success Rate vs. Generation (per-seed).
    print data

    # Plot the data.
    plot = data.plot(kind='line', legend=True)
    plot.set_ylabel(options.get('y', 'Success Rate'))
    plot.set_xlabel(options.get('x', 'Generation'))
    plot.set_title(options.get('title', 'Success Rate vs. Generation'))

    return plot    # success vs. generation
