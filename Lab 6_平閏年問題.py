#!/usr/bin/env python
# coding: utf-8

# In[1]:


y = int(input('请输入年份: '))
if y % 400 == 0:
    print(y, "是闰年")
elif y % 100 == 0:
    print(y, "是平年")
elif y % 4 == 0:
    print(y, '是闰年')
else:
  print(y, "是平年")


# In[ ]:




