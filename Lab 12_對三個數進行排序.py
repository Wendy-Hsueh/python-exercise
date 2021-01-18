#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("請輸入數字:")
m=int(input())
n=int (input())
p=int (input())
sum=m+n+p
if m>n>p:
    print(p,n,m,sum)
elif m>p>n:
    print(n,p,m,sum)
elif n>m>p:
    print(p,m,n,sum)
elif n>p>m:
    print(m,p,n,sum)
elif p>m>n:
    print(n,m,p,sum)
elif p>n>m:
    print(m,n,p,sum)
    


# In[ ]:




