#!/usr/bin/env python
# coding: utf-8

# In[2]:


def compute(a, b):
    if b == 0: return a
    else: return compute(b, a % b)

x= int(input())
y= int(input())
m= int(input())
n= int(input())

a = (x * n) + (m * y)
b=y * n
num = compute(a, b)
print('{}/{} + {}/{} = {}/{}'.format(x, y, m, n, int(a / num), int(b / num)))


# In[ ]:




