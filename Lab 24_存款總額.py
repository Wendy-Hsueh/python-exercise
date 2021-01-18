#!/usr/bin/env python
# coding: utf-8

# In[4]:


m=1
print("請輸入金額:")
a=int(input())
print("請輸入年收益率:")
b=float (input())
print("請輸入經過的月份數:")
c=int(input())
for i in range(c):
    d=a + a * b / 1200
   
    print(m,"    ",d )
    a=d
    m=m+1


# In[ ]:




