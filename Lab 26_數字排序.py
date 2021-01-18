#!/usr/bin/env python
# coding: utf-8

# In[7]:


array= []
for i in range( 10 ):
    num = int( input() )
    array.append(num)    #加入數字到陣列
sortarray2 = sorted( array )  #排序
print("最大的三個值，由大到小排序:")
print (sortarray2[-1],sortarray2[-2],sortarray2[-3])


# In[ ]:




