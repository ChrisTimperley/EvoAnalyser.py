from log_file import *
from data_set import DataSet
from data_frame import DataFrame
from grouped_data_sets import GroupedDataSets
from visualise import visualise

import pprint as pp

import problem
import visualisation
import representation

log = LogFile.read("test.log")

# associated meta-data.
#ds = DataSet(log.data)
df = DataFrame.build(log.data)

pp.pprint(df.table(True))

#visualise(ds, "median_fitness_vs_generation", {
#    'axis': [0, 10, 0.0, 10.0]
#})

#visualise(ds, "mean_fitness_vs_generation")

# .analyse("diversity", { "measure": "normalised_levenshtein" })

# .with("canonical", lambda p: normalise(p.genome))
# .with("distance_to_origin")

# .with_as("canonical", "canonical")
# .with("distance_to_origin")

# virtual_property("canonical") ->
# - requires_representation_is("patch")
# - requires_property("genome")
# - requires_meta_property("problem")

# .transform("relative_distance_matrix")
# .transform("mean")
# .transform("median")
# .transform("max")
# .transform("min")

# Analysis name
# - algorithm type
# - problem type
# - genome requirements
# - fitness requirements
