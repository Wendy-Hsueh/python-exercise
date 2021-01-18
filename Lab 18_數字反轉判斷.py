#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = input()
if num!='0':
    for i in range(len(num)-1,-1,-1):
        print(num[i],end='')
else:
    print(int(num))


# In[ ]:




