from pprint import pprint
from log_file import *
from genetic_algorithm_log import *
import visualisation

log = LogFile.read("test.log")

vis = visualisation.FitnessBoxPlot()

pprint(vis.prepare(log.data))

vis.visualise(log.data)

# Analysis name
# - algorithm type
# - problem type
# - genome requirements
# - fitness requirements
# - view required
