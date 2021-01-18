#!/usr/bin/env python
# coding: utf-8

# In[11]:


def compute(a,x,y):
    for i in range(y):
        print("{} ".format(a)*x)

a = input()
x = int( input() )
y = int( input() )
compute( a , x , y )


# In[ ]:




