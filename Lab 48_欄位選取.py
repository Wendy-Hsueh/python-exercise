# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
csv_file = "D://walk1.csv"
csv_file2 = "D://walk2.csv"
data = pd.read_csv(csv_file)
data2 = pd.read_csv(csv_file2)
a = data.iloc[:,2:5]
b = data2.iloc[:,2:5]
print(a)
print(b)