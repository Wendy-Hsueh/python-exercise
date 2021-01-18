#!/usr/bin/env python
# coding: utf-8

# In[15]:


import csv
oldlist = []
newlist = []
with open(r'C:\Users\User\Downloads\DB.txt', newline='')as csvfile:
    f2 = open('ItemIDList.txt','w')
    f3 = open('DB_ItemID.txt','w')
    f = csv.reader(csvfile)
    for line in f:
        print()
        for j in line:
            oldlist.append(j)
            for i in oldlist:
                if i not in newlist:
                    newlist.append(i)
                    f2.write(i)
                    f2.write(':')
                    c = newlist.index(i)+1
                    f2.write(str(c))
                    f2.write('\n')
                    
                if j in newlist:
                        j = newlist.index(j)+1
                        f3.write(str(j))
                        f3.write(" ")
                        
                
                 

f2.close()
f3.close()


# In[ ]:





# In[ ]:




