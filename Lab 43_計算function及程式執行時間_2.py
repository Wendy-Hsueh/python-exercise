#!/usr/bin/env python
# coding: utf-8

# In[4]:


import time as t

def CountF1(S):
    return True
def GenC2(c):
    return True
def CountC2(L):
    return True
oldlist = []
newlist = []
list3 = []
new_set=[]
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
        if i not in newlist:
                newlist.append(i)
                for j in newlist:
                    if i != j:
                        a = str(newlist.index(i))+str(newlist.index(j))
                        list3.append(a)
    new_set = list(set(list3))
    c = sorted(new_set)
    GenC2(c)
    L=len(new_set)
    CountC2(L)
print(str(t.clock()))
f.close()
f2.close()
f3.close()


# In[ ]:





# In[ ]:




