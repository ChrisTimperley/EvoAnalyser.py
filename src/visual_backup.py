import numpy
from scipy import stats
import matplotlib.pyplot as plt

from entropy import *
from population import Population

def plot_probability_of_solution_after_n_failed_generations(benchmarks, **kwds):
    fig, ax = plt.subplots()

    num_generations = benchmarks[0].generations()
    generations = range(num_generations + 1)

    for benchmark in benchmarks:
        plt.plot(generations,
                 benchmark.probability_of_solution_after_n_failed_generations(),
                 label=benchmark.name) 
    
    plt.title('Probability of success after N failed generations')
    plt.xlabel('No. Failed Generations')
    plt.ylabel('Success Rate')
    plt.axis([0, num_generations, 0.0, 1.0])
    plt.grid(True)

    # Legend
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    # Put a legend to the right of the current axis
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()

def plot_success_rate_vs_generation(runs, **kwds):
    fig, ax = plt.subplots()
    plt.plot(range(runs.generations() + 1), runs.success_rate_vs_generation(), label='GCD')
    plt.title('No. Generations to Success')
    plt.xlabel('Generation')
    plt.ylabel('Success Rate')
    plt.axis([0, runs.generations(), 0.0, 1.0])
    plt.grid(True)

    # Legend
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    # Put a legend to the right of the current axis
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()

def plot_mean_fitness_vs_generation(runs, **kwds):

    # Coerce to list.
    if isinstance(runs, Benchmark):
        runs = runs.runs
    elif not isinstance(runs, list):
        runs = [runs]

    # Get the state of the population at each generation.
    generations = range(len(runs[0].states()))
    mean_fitnesses = map(lambda r: map(numpy.mean, map(lambda s: s.fitnesses(), r.states())),
                           runs)

    # Try to plot each median fitness.
    for fitnesses in mean_fitnesses:
        plt.plot(generations, fitnesses)

    # Add a title to the plot, if one has been provided.
    if kwds.has_key('title'):
        plt.title(kwds['title'])

    plt.xlabel('Generation')
    plt.ylabel('Mean Fitness')
    #plt.axis([0, generations[-1]])
    plt.grid(True)
    plt.show()

def plot_relative_normalised_distance_vs_generation(runs, **kwds):
    kwds['normalised'] = True
    plot_relative_distance_vs_generation(runs, **kwds)

def plot_relative_distance_vs_generation(runs, **kwds):

    # Coerce to list.
    if isinstance(runs, Benchmark):
        runs = runs.runs
    elif not isinstance(runs, list):
        runs = [runs]

    # Set up the transformation function.
    transform_label, transform = ({
        'mean': ('Mean', numpy.mean),
        'mode': ('Mode of', stats.mode),
        'median': ('Median of', numpy.median),
        'max': ('Max.', max),
        'min': ('Min.', min)
    })[kwds.get('transform', 'mean')]

    # Fetch the problem.
    problem = runs[0].problem

    if kwds.has_key('normalised') and kwds['normalised']:
        dist_fun = lambda s: s.relative_normalised_distances(problem)
        plt.ylabel('%s Relative Normalised Distance' % (transform_label))
    else:
        dist_fun = lambda s: s.relative_distances(problem)
        plt.ylabel('%s Relative Distance' % (transform_label))

    generations = range(len(runs[0].states()))
    distances = map(lambda r: map(dist_fun, r.states()), runs)
    mean_distances = map(lambda r: map(transform, r), distances)

    # Plot each of the lines.
    for distances in mean_distances:
        plt.plot(generations, distances)

    # Add a title to the plot, if one has been provided.
    if kwds.has_key('title'):
        plt.title(kwds['title'])

    plt.xlabel('Generation')
    plt.grid(True)
    plt.show()

def plot_distance_to_origin_vs_generation(runs, **kwds):

    # Coerce to list.
    if isinstance(runs, Benchmark):
        runs = runs.runs
    elif not isinstance(runs, list):
        runs = [runs]

    # Fetch the problem.
    problem = runs[0].problem

    # Get the state of the population at each generation.
    generations = range(len(runs[0].states()))
    distances = map(lambda r: map(lambda s: s.distances_to_origin(problem), r.states()), runs)
    mean_distances = map(lambda r: map(numpy.mean, r), distances)

    # Plot each of the lines.
    for distances in mean_distances:
        plt.plot(generations, distances)

    # Add a title to the plot, if one has been provided.
    if kwds.has_key('title'):
        plt.title(kwds['title'])

    plt.xlabel('Generation')
    plt.ylabel('Mean Distance to Origin')
    plt.grid(True)
    plt.show()

def plot_probability_of_solution_vs_generation(benchmarks):
    if not isinstance(benchmarks, list):
        benchmarks = [benchmarks]
    
    # Assume the same number of generations across all benchmarks.
    generations = range(benchmarks[0].generations() + 1)

    fig, ax = plt.subplots()

    for benchmark in benchmarks:
        plt.plot(generations,
                 benchmark.probability_of_solution_vs_generation(),
                 label=benchmark.name)

    # Legend
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.axis([0, benchmarks[0].generations(), 0.0, 1.0])
    plt.xlabel('Generation')
    plt.ylabel('Probability of solution')
    plt.grid(True)
    plt.show()

def plot_probability_of_solution_after_n_generations(benchmarks):
    if not isinstance(benchmarks, list):
        benchmarks = [benchmarks]
    
    # Assume the same number of generations across all benchmarks.
    generations = range(benchmarks[0].generations() + 1)

    fig, ax = plt.subplots()

    for benchmark in benchmarks:
        plt.plot(generations,
                 benchmark.probability_of_solution_after_n_generations(),
                 label=benchmark.name)

    # Legend
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.axis([0, benchmarks[0].generations(), 0.0, 1.0])
    plt.xlabel('Generation')
    plt.ylabel('Probability of finding a solution')
    plt.grid(True)
    plt.show()


# Produces a boxplot of the number of unique solutions found during a run from
# a set of runs on a given benchmark.
def num_unique_solutions_boxplot(runs):
    plt.boxplot(runs.num_unique_solutions_per_run(), 1)
    plt.ylabel('Num. Unique Solutions')
    plt.title('Number of unique solutions found during a single run.')
    plt.show()

# Produces a box-plot of the redundancy for a set of runs on a given
# benchmark.
def redundancy_boxplot(runs):
    plt.boxplot(runs.redundancies(), 1)
    plt.ylabel('Redundancy')
    plt.show()

def site_entropies_boxplot(runs):
    problem = runs.problem
    stmts = problem.statements()

    sites = [[] for s in stmts]
    for run in runs.runs:
        for (i, h) in enumerate(run.site_entropies()):
            sites[i].append(h)

    fig, ax1 = plt.subplots(figsize=(10,6))
    fig.canvas.set_window_title("Site entropy across multiple runs")

    plt.setp(ax1, xticklabels=stmts)
    plt.boxplot(sites)
    plt.title("Site entropy across multiple runs")
    plt.ylabel('Entropy')
    plt.xlabel('Site ID')
    plt.show()

def site_entropy_vs_generation(runs, sid):
    problem = runs.problem
    num_generations = len(runs.runs[0].states())
    generations = range(num_generations)

    # Plot the entropy for each run.
    for run in runs.runs:
        entropies = map(lambda s: s.site_entropy(problem, sid), run.states())
        plt.plot(generations, entropies)

    plt.xlabel('Generation')
    plt.ylabel('Site Entropy')
    plt.grid(True)
    plt.show()
