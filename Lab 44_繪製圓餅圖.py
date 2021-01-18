# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
list_labels =["Taichung","English","Taipei","Ilan"]
list_size = [30.00,10.00,50.00,10.00]
list_colors = ["blue","green","yellow","red"]

explode=(0.1,0,0,0)

plt.pie(list_size,
        explode=explode,
        labels=list_labels,
        colors=list_colors,
        labeldistance=1.1,
        autopct="%1.2f%%",
        shadow=True,
        startangle=40,
        pctdistance=0.6)
plt.axis("equal")
plt.legend()
plt.show()
