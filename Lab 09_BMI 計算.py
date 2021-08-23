#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=float(input(" 身高 :"))
y=float(input(" 體重 :"))
x=x/100
z=y/(x*x)
if z<18.5:
   print(z,"體重過輕")
elif z>=18.5 and z<24:
    print(z,"健康體位")
elif z>24:
    print(z,"體重過重")


# In[ ]:




