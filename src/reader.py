from log_file import *
from visualise import visualise
from glob import glob

import problem
import visualisation
import representation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the log file for each run.
logs = map(LogFile.read, glob('../examples/gcd/*.log'))
logs = map(lambda l: l.data, logs)
logs = pd.concat(logs)

# How many unique patches are there?
num = len(logs)
unique = len(pd.unique(logs['canonical'].values.ravel()))

ratio = float(unique) / num
print ratio

# Let's try some visualisations :-)
visualise("mean_distance_to_origin_vs_generation", logs)
plt.show()
