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
#logs = map(LogFile.read, glob('../examples/gcd/*.log'))
#logs = map(lambda l: l.data, logs)
#logs = map(pd.DataFrame, logs)
#logs = pd.concat(logs)

logs = LogFile.read("test.log")
logs = logs.data
logs = pd.DataFrame(logs)

print logs

# Mean fitness vs. Generation (many runs)
logs.groupby('generation').aggregate(np.mean)['fitness'].plot(kind='line')
plt.show()
