import numpy
import sys
import glob
import os
import matplotlib.pyplot as plt

from visual import *
from utility import *
from entropy import *
from distance import *
from population import *
from fix import Fix
from patch import Patch
from intermediate import Intermediate
from problem import Problem
from individual import Individual
from initialisation import Initialisation
from generation import Generation
from run import Run
from benchmark import Benchmark

class LogFile:

    # Reads the contents of a given log file, or directory of log files,
    # at a given address, returning them as a list.
    @staticmethod
    def read(fn):
        return LogFile.read_dir(fn) if os.path.isdir(fn) else [LogFile.read_file(fn)]


    # Loads all the log files for a given benchmark from a specified
    # directory, and returns them as a Benchmark object.
    @staticmethod
    def load_benchmark(name, dir_name):
        print "Loading benchmark: %s" % (name)
        return Benchmark(name, LogFile.read_dir(dir_name))

    # Reads the contents of all the log files within a given directory,
    # returning them as a list.
    @staticmethod
    def read_dir(dir_name):
        print "Reading directory: %s" % (dir_name)
        return map(LogFile.read_file,
                   glob.glob("%s/*.log" % dir_name))

    # Reads the contents of a log file at a given location.
    @staticmethod
    def read_file(fn):
        print "Reading log file: %s" % (fn)

        # Read the contents of the log file to a string and split it using
        # each of its section dividers.
        with open(fn, "r") as f:
            sections = (f.read().split("=" * 80))[1:]

        # Parse each section.
        problem = Problem.from_string(sections.pop(0))
        initialisation = Initialisation.from_string(problem, sections.pop(0))
        generations = []
        while sections:
            generations.append(Generation.from_string(problem, sections.pop(0)))

        # Build the run object.
        return Run(problem, initialisation, generations)

# Find the names of the log files from the list of arguments.
benchmarks = [
    LogFile.load_benchmark("gcd", "gcd/"),
    LogFile.load_benchmark("zune", "zune/")
]

plot_probability_of_solution_after_n_failed_generations(benchmarks)
#plot_probability_of_solution_vs_generation(benchmarks)
#plot_probability_of_solution_after_n_generations(benchmarks)
#num_unique_solutions_boxplot(runs)
#plot_prob_success_after_n_failed_generations(runs)
#plot_success_rate_vs_generation(runs)
#site_entropies_boxplot(runs)
#site_entropy_vs_generation(runs, 12)
#plot_relative_normalised_distance_vs_generation(runs, transform="median")
#plot_relative_distance_vs_generation(runs)
#plot_distance_to_origin_vs_generation(runs)
#redundancy_boxplot(benchmark)
#plot_mean_fitness_vs_generation(runs.runs)
