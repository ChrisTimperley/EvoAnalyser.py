import numpy
import sys

from entropy import *
from intermediate import Intermediate
from utility import *
from distance import *
from collections import Counter

class Population:

    # Constructs a new Population object given an ordered list of individuals
    # belonging to that population.
    def __init__(self, contents):
        self.contents = contents
        self._size = len(contents)
        self._relative_distance_matrix = None
        self._relative_normalised_distance_matrix = None
        self._distances_to_origin = None

    # Returns true if this population contains an acceptable solution to the
    # problem.
    def found_solution(self, problem):
        return any(problem.is_ideal_fitness(i.fitness) for i in self.contents)

    # Returns a list of each of the ideal solutions within this population.
    def ideal_solutions(self, problem):
        inds = filter(lambda i: problem.is_ideal_fitness(i.fitness),
                      self.contents)
        return uniq(map(lambda i: i.canonical_patch, inds))

    # Returns the size of the population.
    def size(self):
        return self._size

    # Returns a list of the normalised genomes within this population,
    # along with their fitness values.
    def normalised_genomes_with_fitness(self, problem):
        return map(lambda i: (i.patch.normalise(problem), i.fitness),
                   self.contents)

    # Returns a list of the genomes within this population, along with
    # their fitnesses.
    def genomes_with_fitness(self):
        return map(lambda i: (i.patch, i.fitness), self.contents)

    # Returnsa  list of the genomes of each of the individuals within this
    # population.
    def genomes(self):
        return map(lambda i: i.patch, self.contents)

    # Returns a list of the fitnesses of each of the individuals within this
    # population.
    def fitnesses(self):
        return map(lambda i: i.fitness, self.contents)

    # Calculates the entropy of a specific site across the population.
    def site_entropy(self, problem, sid):
        return site_entropy(problem, map(lambda g: Intermediate.from_patch(problem, g),
                                         self.genomes()), sid)

    # Calculates the entropy at each site across the population.
    def site_entropies(self, problem):
        return site_entropies(problem, self.genomes()) 

    # Calculates the distance between each member of the population and the
    # origin.
    def distances_to_origin(self, problem):
        if not self._distances_to_origin:
            patches = map(lambda i: i.patch, self.contents)
            self._distances_to_origin = distances_from_origin(problem, patches)
        return self._distances_to_origin

    # Calculates the relative distance matrix for this population.
    def relative_distance_matrix(self, problem):
        if not self._relative_distance_matrix:
            metric = lambda x, y: levenshtein(x.to_lines(problem), y.to_lines(problem))
            mat = distance_matrix(map(lambda i: i.patch, self.contents), metric)
            self._relative_distance_matrix = mat
        return self._relative_distance_matrix
 
    # Calculates the relative distance matrix for this population.
    def relative_normalised_distance_matrix(self, problem):
        if not self._relative_normalised_distance_matrix:
            metric = lambda x, y: normalised_levenshtein(x.to_lines(problem), y.to_lines(problem))
            mat = distance_matrix(map(lambda i: i.patch, self.contents), metric)
            self._relative_normalised_distance_matrix = mat
        return self._relative_normalised_distance_matrix

    # Returns a list of the unique (i.e. d(x,y) but not d(y,x)) relative
    # absolute distances between individuals within this population.
    def relative_distances(self, problem):
        mat = self.relative_distance_matrix(problem)
        distances = []
        for y in range(2, self._size):
            for x in range(y):
                distances.append(mat[y][x])
        return distances

    # Returns a list of the relative (normalised) distances between individuals
    # within this population.
    def relative_normalised_distances(self, problem):
        mat = self.relative_normalised_distance_matrix(problem)
        distances = []
        for y in range(2, self._size):
            for x in range(y):
                distances.append(mat[y][x])
        return distances

    # Transforms the contents of this population into a string format.
    def to_string(self):
        return '\n'.join(map(IndividualInfo.to_string, self.contents))

    def entropy_to_string(self):
        dbg = ', '.join(map(lambda h: "%0.4f" % (h), self.site_entropies()))
        avg_site_entropy = numpy.mean(self.site_entropies())
        return "%0.4f = %s" % (avg_site_entropy, dbg)
