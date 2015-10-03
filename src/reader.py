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

# Mean fitness vs. Generation (many runs)
#frame.groupby('generation').aggregate(max)['fitness'].plot(kind='line')
#plt.show()
