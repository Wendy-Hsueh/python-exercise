#!/usr/bin/env python
# coding: utf-8

# In[33]:


def CountF1(S):
    print(a)
oldlist = []
newlist = []
S={}
f = open(r'C:\Users\User\Downloads\DB.txt')
f2 = open('ItemIDList.txt','w')
f3 = open('DB_ItemID.txt','w')
for line in f:
    print()
    for j in line.split(","):
        oldlist.append(j)
    for i in oldlist:
        if oldlist.count(i)>=1:
            S[i] = oldlist.count(i)
CountF1(S)                   
f.close()
f2.close()
f3.close()


# In[ ]:




