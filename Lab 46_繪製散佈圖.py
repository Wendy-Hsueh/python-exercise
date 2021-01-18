# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

a = [0,0,0,1,1.3,1.5,2,2.2,2.6,3.2,4.1,4.4,4.4,5]
b = [87,89,91,90,82,80,78,81,76,85,80,75,73,72]
plt.xlabel("hour_phone_used")
plt.ylabel("work_performance")
plt.scatter(a, b)
plt.show()