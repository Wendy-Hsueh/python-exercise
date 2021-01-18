#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("請輸入數字:")
score = int( input() )

while score!= -9999:
    print("GPA:")
    if  90 <= score <= 100: 
        print('A')
    elif 80 <= score <= 89:
        print('B')
    elif 70 <= score <= 79:
        print('C')
    elif 60 <= score <= 69:
        print('D')
    else:
        print('E')
    print("請輸入數字:")
    score = int( input() )


# In[ ]:




