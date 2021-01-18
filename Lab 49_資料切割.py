# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:26:17 2019

@author: E306
"""

import pandas as pd
import numpy as np

csv_file = "D://walk1.csv"
csv_file2 = "D://walk2.csv"
data = pd.read_csv(csv_file)
data2 = pd.read_csv(csv_file2)

def window_stack(d, w, t):
    r = np.arange(len(d))
    s = r[::t]
    z = list(zip(s,s+w))
    f = '{0[0]}:{0[1]}'.format
    g = lambda t: d.iloc[t[0]:t[1]]
    return pd.concat(map(g,z),keys=map(f,z))


pp = window_stack(data, w=4, t=2)
gg = window_stack(data2, w=4, t=2)
print(pp.iloc[:])
print(gg.iloc[:])