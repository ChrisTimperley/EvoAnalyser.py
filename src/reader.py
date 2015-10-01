from log_file import *
from genetic_algorithm_log import *
from data_set import DataSet
from grouped_data_sets import GroupedDataSets
from visualise import visualise
import visualisation

log = LogFile.read("test.log")
ds = DataSet(log.data)

visualise(ds, "mean_fitness_vs_generation", {
    'axis': [0, 10, 0.0, 10.0]
})

# Analysis name
# - algorithm type
# - problem type
# - genome requirements
# - fitness requirements
