#!/usr/bin/env python
# coding: utf-8

# In[11]:


def compute(a, b, c):
    d = (b**2) - (4 * a * c)

    if d > 0:
        x = (-b + (d**0.5)) / (2 * a)
        y = (-b - (d**0.5)) / (2 * a)
        return x, y
    else:
        return 'Your equation has no root.', None

a = eval( input() )
b = eval( input() )
c = eval( input() )
m,n = compute( a , b , c )

if n == None:
    print(m)
else:
    print('{}, {}'.format(m, n))


# In[ ]:




