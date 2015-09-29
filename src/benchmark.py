from entropy import *
from utility import *
from run import Run
from collections import Counter

# Stores information about multiple runs of an EA with identical settings on
# the same problem.
class Benchmark:

    # Constructs a new benchmark object.
    def __init__(self, name, runs):
        self.name = name
        self.problem = runs[0].problem
        self.runs = runs

    # Returns the number of generations performed for each run.
    def generations(self):
        return len(self.runs[0].generations)
    
    # Returns a list describing the number of unique solutions found during
    # each run in this set.
    def num_unique_solutions_per_run(self):
        return map(Run.num_unique_solutions, self.runs)

    def probability_of_solution_after_n_failed_generations(self):
        ss = map(Run.successful_states, self.runs)
        p = []
        for g in range(self.generations() + 1):
            fails = filter(lambda s: (not s) or s[0] >= g, ss)
            later_successes = filter(lambda s: s, fails)
            fails = float(len(fails))
            later_successes = len(later_successes)
            p.append(later_successes / fails if fails > 0.0 else 0.0)
        return p

    # Calculates the probability of a solution being found at each generation.
    def probability_of_solution_vs_generation(self):
        n = float(len(self.runs))
        p = []
        counter = Counter()
        for run in self.runs:
            counter.update(run.successful_states())
        counter = dict(counter)
        for g in range(self.generations() + 1):
            p.append(counter[g] / n if counter.has_key(g) else 0.0)
        return p

    # Calculates the probability of a solution being found after n - 1
    # generations have passed.
    def probability_of_solution_after_n_generations(self):
        n = float(len(self.runs))
        p = []
        for g in range(self.generations() + 1):
            s = len(filter(lambda r: r.solution_found_after_n_generations(g, True),
                           self.runs))
            p.append(s / n)
        return p

    def successes_vs_generation(self):
        successes = map(Run.generations_to_success, self.runs)
        successes = filter(lambda g: not g is None, successes)
        successes = dict(Counter(successes))

        # Assume that all runs are for the same number of generations.
        cumulative = 0
        svg = [0] * (self.generations() + 1)

        for g in range(self.generations() + 1):
            if successes.has_key(g):
                cumulative += successes[g]
            svg[g] = cumulative

        return svg

    def success_rate_vs_generation(self):
        n = float(len(self.runs))
        return map(lambda s: s / n, self.successes_vs_generation())

    # Calculates the entropy at each site across all individuals in all
    # runs belonging to this set.
    def site_entropies(self): 
        return site_entropies(self.problem, self.genomes())

    # Returns a list of all the ideal solutions found during this run, in their
    # canonical form.
    def ideal_solutions(self):
        return uniq([s for run in self.runs for s in run.ideal_solutions()])

    # Returns a list of the normalised genomes within this run, along
    # with their fitness values.
    def normalised_genomes_with_fitness(self):
        gf = [r.normalised_genomes_with_fitness() for r in self.runs]
        return flatten(gf)

    # Returns an ordered list of each genome encountered across the run of the
    # EA coupled with their respective fitnesses.
    def genomes_with_fitness(self):
        gf = [r.nomalised_genomes_with_fitness() for r in self.runs]
        return flatten(gf)

    # Returns list of every genome visited (with redundancy) by each run in
    # this set.
    def genomes(self):
        return [g for run in self.runs for g in run.genomes()]

    # Returns list of each fitness value encountered by each run in
    # this set.
    def fitnesses(self):
        return [f for run in self.runs for f in run.fitnesses()]

    # Returns the redundancies of each of the runs in this set.
    def redundancies(self):
        return map(Run.redundancy, self.runs)
