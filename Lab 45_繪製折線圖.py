# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
A = [random.randint(1, 20) for _ in range(10)]  
B = [random.randint(1, 20) for _ in range(10)] 
plt.plot(A,color="blue",lw="5.0",ls="--",label="A")
plt.plot(B,color="red",lw="5.0",ls="--",label="B")
plt.legend()
plt.show()