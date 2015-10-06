import matplotlib.pyplot as plt
import numpy as np

def __problem_success_rate_vs_generation(data):
    # Success vs. Generation (per-seed).
    data = data.groupby('seed')
    data = data.apply(lambda g: g.groupby('generation')['ideal'].max().cummax().map(np.float) )
    return data.apply(np.mean)

def success_rate_vs_generation(data, options = {}):
   
    # Generate the success rate for each problem.
    data = data.groupby('problem').apply(__problem_success_rate_vs_generation)
    data = data.unstack().reset_index()
    data.columns = ['generation', 'problem', 'success_rate']
    data = data.groupby('problem')

    # Plot each line.
    fig, ax = plt.subplots()
    labels = []
    for name, sub in data:
        ax = sub.plot(ax=ax, x='generation', y='success_rate')
        labels.append(name)
    lines, _ = ax.get_legend_handles_labels()
    ax.set_xlabel(options.get('x', 'Generations Passed'))
    ax.set_ylabel(options.get('y', 'Success Rate'))
    ax.set_title(options.get('title', 'Success Rate vs. Generations Passed'))
    ax.legend(lines, labels, loc='best')
    ax.grid(True)
    ax.set_ylim([0.0, 1.0])
    return fig
