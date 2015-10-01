from pprint import pprint
from log_file import *
from genetic_algorithm_log import *
from data_set import DataSet
from grouped_data_sets import GroupedDataSets

import visualisation

log = LogFile.read("test.log")
ds = DataSet(log.data)

pprint(ds.project("fitness").contents())

# Analysis name
# - algorithm type
# - problem type
# - genome requirements
# - fitness requirements
# - view required
