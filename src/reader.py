from log_file import *
from genetic_algorithm_log import *

log = LogFile.read("test.log")
glog = GeneticAlgorithmLog.process(log)

# Process each point within the search according to the problem type and
# algorithm.

# individual (evolutionary algorithm)
# .generation
# .position
# .deme
# .genome (process according to problem type?)
# .fitness (process according to fitness scheme)

# Create different views on the same data:
# - grouped by deme
# - grouped by generation
# - grouped by deme and generation
# - any view you like
# - cache these views
