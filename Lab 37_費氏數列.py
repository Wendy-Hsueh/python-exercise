#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def compute(n):
    if n < 2:
        return n
    else:
        return compute(n-1)+compute(n-2)

num = int( input() )
for i in range(num):
    print( compute(i),end=' ')
      


# In[ ]:




