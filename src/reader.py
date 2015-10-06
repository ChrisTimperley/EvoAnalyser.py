from log_file import *
from glob import glob

import problem
import visualisation
import representation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    logs = map(LogFile.read, glob('../examples/gcd/*.log'))
    logs += map(LogFile.read, glob('../examples/indent/*.log'))
    logs += map(LogFile.read, glob('../examples/flex/*.log'))
    logs += map(LogFile.read, glob('../examples/uniq/*.log'))
    logs += map(LogFile.read, glob('../examples/units/*.log'))
    logs += map(LogFile.read, glob('../examples/zune/*.log'))
    logs = map(lambda l: l.data, logs)
    return pd.concat(logs)

# How many solutions did we find across all runs?
#num_solutions = np.count_nonzero(logs['ideal'])

# How many unique patches are there?
#num = len(logs)
#unique = len(pd.unique(logs['canonical'].values.ravel()))
#ratio = float(unique) / num
#print ratio
