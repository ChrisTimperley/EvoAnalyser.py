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

# Mean fitness vs. Generation (many runs)
gens = logs.groupby('generation')
gs = gens.apply(lambda g: g.groupby('seed').aggregate(np.mean)['fitness'])
plot = gs.plot(kind='line', legend=False)
plot.set_ylabel('Fitness')
plot.set_xlabel('Generation')
plot.set_title('Mean Fitness vs. Generation (GCD)')
plt.show()
