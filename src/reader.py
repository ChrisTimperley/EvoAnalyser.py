from pprint import pprint
from log_file import *
from genetic_algorithm_log import *

log = LogFile.read("test.log")

#
fitnesses = map(lambda p: p.fitness, log.data)

pprint(fitnesses)
