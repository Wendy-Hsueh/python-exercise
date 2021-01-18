#!/usr/bin/env python
# coding: utf-8

# In[50]:


f = open(r'C:\Users\User\Downloads\DB.txt')
cnt = 0
cnt2 = 0
print('每筆交易:')
for line in f:
    print(line,end="") 
    
    for j in line.split(","):
        cnt2 += 1
    cnt += 1


print()
print('總交易筆數:',cnt)
print('總商品個數:',cnt2)
f.close()


# In[39]:


C:\Users\User\Downloads


# In[ ]:




