# Population best fitness vs. generation (multiple seeds)
def pbest_fitness_vs_generation(data, options = {}):
    data = data.groupby('generation')
    data = data.apply(lambda g: g.groupby('seed')['fitness'].max())

    # Plot the data.
    plot = data.plot(kind='line', legend=False)
    plot.set_ylabel(options.get('y', 'Population Best Fitness'))
    plot.set_xlabel(options.get('x', 'Generation'))
    plot.set_title(options.get('title', 'Population Best Fitness vs. Generation'))

    return plot

# Constructs a line graph showing the fitness of the best solution found so far
# during the search against the current generation. Each seed for the problem
# problem is given its own line.
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
