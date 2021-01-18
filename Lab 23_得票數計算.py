#!/usr/bin/env python
# coding: utf-8

# In[12]:


cnt1=0
cnt2=0
cnt3=0
for i in range(5):
    print("No.1: Nami,No.2: Chopper，請輸入1或2:")
    
    a=int(input ())
    if a==1:
        cnt1+=1
    elif a==2:
        cnt2+=1
    else:
        cnt3+=1
    print("Total votes No.1:Nami=",cnt1)
    print("Total votes No.2:Chopper=",cnt2)
    print("Total null votes =",cnt3)
if cnt1>cnt2:
    print("=>No.1 Nami won the election.")
elif cnt2>cnt1:
    print("=>No.2 Chopper won the election.")
else :
    print("=> No one won the election.")


# In[ ]:




