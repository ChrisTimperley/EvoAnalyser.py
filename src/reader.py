import numpy as np
from pprint import pprint
from log_file import *
from genetic_algorithm_log import *
from data_set import DataSet
from grouped_data_sets import GroupedDataSets

import visualisation

log = LogFile.read("test.log")
ds = DataSet(log.data)

pprint(ds.project("fitness").contents())

# Let's try and find all the fitness values from the 1st generation.
fitness_gen = ds.group_by("generation").project("fitness")

mean_fitness_gen = fitness_gen.transform(lambda d: np.mean(d.items()))

# Analysis name
# - algorithm type
# - problem type
# - genome requirements
# - fitness requirements
# - view required
