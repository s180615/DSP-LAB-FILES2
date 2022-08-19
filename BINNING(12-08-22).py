#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv("ab.csv")
print(df)


# In[2]:


s=df['POINTS_bin']=pd.qcut(df['POINTS'],q=3)
print(s)


# In[3]:


w=df['POINTS_bin'].value_counts()
print(w)


# In[4]:


S=df["POINTS_bin"]=pd.qcut(df['POINTS'],q=[0,0.2,0.4,0.6,0.8,1],labels=['A','B','C','D','E'])
print(S)


# In[ ]:




