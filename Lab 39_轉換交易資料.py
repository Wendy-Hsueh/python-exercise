#!/usr/bin/env python
# coding: utf-8

# In[39]:


oldlist = []
newlist = []
f = open(r'C:\Users\User\Downloads\DB.txt')
f2 = open('ItemIDList.txt','w')
f3 = open('DB_ItemID.txt','w')
for line in f:
    print()
    for j in line.split(","):
        oldlist.append(j)
        for i in oldlist:
            if i not in newlist:
                newlist.append(i)
                f2.write(i)
                f2.write(':')
                f2.write(str(newlist.index(i)))
                f2.write('\n')
                if j==i:
                    f3.write(str(newlist.index(i)))
f.close()
f2.close()
f3.close()


# In[ ]:





# In[ ]:




