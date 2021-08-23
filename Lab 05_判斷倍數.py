#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=int(input("請輸入文字")) 
if num%2==0 and num%5==0:
    print('為2,5的倍數')
elif num%2==0 and num%5!=0:
    print('為2的倍數')
elif num%2!=0 and num%5==0:
    print('為5的倍數')
elif num%2!=0 and num%5!=0:
    print('不為2,5的倍數')


# In[ ]:




