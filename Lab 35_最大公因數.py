#!/usr/bin/env python
# coding: utf-8

# In[21]:


def compute( m , n ):
    if n==0:
        return k(m)
    else:
        compute(n , (m%n))

def k(m):
    print(m)
    
x= int(input())
y= int(input())
compute(x,y)                                  


# In[ ]:




