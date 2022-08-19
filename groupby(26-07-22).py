#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df=pd.read_csv("sl.csv")
print(df)


# In[6]:


a=print(df.groupby(["GENDER"]))


# In[3]:


print(df.groupby(["GENDER"]).mean())


# In[4]:


print(df.groupby(["GENDER","DEPT"]))


# In[9]:


a=df.groupby(["GENDER","DEPT"])
print(a)


# In[10]:


print(a.groups)


# In[13]:


print(df.groupby(["DEPT"]).mean())


# In[14]:


print(df.groupby(["DEPT"]).max())


# In[16]:


print(df.groupby(["GENDER"]).max())


# In[17]:


print(df.groupby(["DEPT"]).groups)


# In[18]:


print(df.groupby(["GENDER"]).groups)


# In[19]:


g=df.groupby(["GENDER"])
print(g.get_group("M"))


# In[20]:


print(g.get_group('F'))


# In[21]:


df["GENDER"].value_counts()


# In[ ]:





# In[ ]:




