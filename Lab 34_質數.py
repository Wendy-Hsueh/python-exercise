#!/usr/bin/env python
# coding: utf-8

# In[24]:


x=int(input())

if x > 1:   
       for i in range(2,x):
        if (x % i) == 0:
            print("NotPrime")
            break
        else:
            print("Prime")
               

else:
    print("Not Prime")




# In[ ]:




