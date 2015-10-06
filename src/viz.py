#

# Group by problem.
# - 


# Graphs
# - Cumulative fitness (single problem, generation)
# - search_best_fitness_vs_generation
# - pop_best_fitness_vs_generation

data.groupby('seed').apply(lambda g: g.groupby('generation').['fitness'].max())

# group by seed.
data.groupby('problem')
