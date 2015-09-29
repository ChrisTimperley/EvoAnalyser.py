from entropy import *
from utility import *
from patch import Patch
from collections import Counter

class Run:

    # Constructs a new Run object from the information about the initialisation
    # and generations for a run of an EA on a given problem.
    def __init__(self, problem, initialisation, generations):
        self.problem = problem
        self.initialisation = initialisation
        self.generations = generations
        self._num_visits = reduce(lambda sm, s: sm + s.size(), self.states(), 0)

    def successful_states(self):
        return [i for (i, s) in enumerate(self.states()) if s.found_solution(self.problem)]

    def solution_found_after_n_generations(self, n, inclusive=False):
        ss = self.successful_states()
        return any(x >= n for x in ss) if inclusive else any(x > n for x in ss)

    # Returns how many generations were passed before an acceptable solution
    # was found by this run. If no acceptable solutions were found during this
    # run, then None is returned.
    def generations_to_success(self):
        successes = self.successful_states()
        return min(successes) if successes else None

    # Calculates the entropy at each site across all individuals in the
    # given run.
    def site_entropies(self): 
        return site_entropies(self.problem, self.genomes())

    # Returns the number of unique (ideal) solutions found during this run.
    def num_unique_solutions(self):
        return len(self.ideal_solutions())

    # Returns a list of all the ideal solutions found during this run, in their
    # canonical form.
    def ideal_solutions(self):
       return uniq([s for state in self.states() for s in state.ideal_solutions(self.problem)])

    # Calculates the redundancy of this run, measured by the fraction of
    # evaluations which are redundant.
    def redundancy(self):
        return self.num_normalised_revisits() / float(self.num_visits())

    # Returns the number of individuals encountered across the entire run.
    def num_visits(self):
        return self._num_visits

    # Calculates the number of times that any (normalised) genome is revisited by
    # the search.
    def num_normalised_revisits(self):
        g = map(Patch.to_string, self.normalised_genomes())
        return self.num_visits() - len(set(g))

    # Returns an ordered list of the state of the population following
    # initialisation and each generation of the EA.
    def states(self):
        states = map(lambda g: g.offspring, self.generations)
        return [self.initialisation.population] + states

    # Returns an ordered list of the fitnesses values encountered across this
    # run of the EA.
    def fitnesses(self):
        return map(lambda i: i.fitness, self.individuals())

    # Returns the frequency of each fitness value encountered across this run
    # of the EA, in the form of a dictionary.
    def fitness_frequencies(self):
        h = self.fitness_histogram()
        size = float(sum(h.values()))
        return dict(map(lambda (f, c): (f, c / size), h.items()))

    # Returns the histogram of fitness values encountered across this run of
    # the EA, in the form of a dictionary.
    def fitness_histogram(self):
        return dict(Counter(self.fitnesses()))

    # Returns an ordered list of each genome encountered across the run of
    # the EA.
    def genomes(self):
        return map(lambda i: i.patch, self.individuals())

    # Returns an ordered list of each genome encountered during this run of the
    # EA, in their normalised forms.
    def normalised_genomes(self):
        return map(lambda g: g.normalise(self.problem), self.genomes())

    # Returns a list of the normalised genomes within this run, along
    # with their fitness values.
    def normalised_genomes_with_fitness(self):
        gf = [s.normalised_genomes_with_fitness(self.problem) for s in self.states()]
        return flatten(gf)

    # Returns an ordered list of each genome encountered across the run of the
    # EA coupled with their respective fitnesses.
    def genomes_with_fitness(self):
        return self.population.genomes_with_fitness()

    # Returns an ordered list of every individual encountered across the run of
    # this EA.
    def individuals(self):
        return reduce(lambda inds, s: inds + s.contents, self.states(), [])
