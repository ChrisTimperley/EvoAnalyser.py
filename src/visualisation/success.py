import matplotlib.pyplot as plt
import numpy as np

def __problem_prob_solution_vs_generation(data):
    data = data.groupby('seed')
    data = data.apply(lambda g: g.groupby('generation')['ideal'].max().map(np.float) )
    return data.apply(np.mean)

def __problem_success_rate_vs_generation(data):
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

def prob_solution_vs_generation(data, options = {}):
    # Generate the success rate for each problem.
    data = data.groupby('problem').apply(__problem_prob_solution_vs_generation)
    data = data.unstack().reset_index()
    data.columns = ['generation', 'problem', 'probability']
    data = data.groupby('problem')

    # Plot each line.
    fig, ax = plt.subplots()
    labels = []
    for name, sub in data:
        ax = sub.plot(ax=ax, x='generation', y='probability')
        labels.append(name)
    lines, _ = ax.get_legend_handles_labels()
    ax.set_xlabel(options.get('x', 'Generation'))
    ax.set_ylabel(options.get('y', 'Probability of Solution'))
    ax.set_title(options.get('title', 'Probability of finding a solution at each generation'))
    ax.legend(lines, labels, loc='best')
    ax.grid(True)
    ax.set_ylim([0.0, 1.0])
    return fig

def num_unique_solutions_vs_problem(data, options = {}):
    data = data.groupby('problem')
    data = data.apply(lambda g: len(g[g['ideal']]['canonical'].unique()))
    plot = data.plot(kind='bar')
    plot.set_xlabel(options.get('x', 'Problem'))
    plot.set_ylabel(options.get('y', 'No. Unique Solutions Found'))
    plot.set_title(options.get('title', 'Number of unique solutions found for each problem across all runs'))
    return plot
