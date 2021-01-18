#!/usr/bin/env python
# coding: utf-8

# In[4]:


cnt = 0
list1 = [ "A", "J", "Q", "K"]
list2 = [ 1, 11, 12, 13 ]
for i in range(5):
    a = input()
    if a in list1: 
        cnt += list2[ list1.index( a ) ]
    else: 
        cnt += int( a )

print( cnt )


# In[ ]:




