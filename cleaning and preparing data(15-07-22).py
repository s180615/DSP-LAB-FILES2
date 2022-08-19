#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
a=pd.DataFrame({"Name":["Lavanya","Mahi","siri","teju"],"Age":["18","17","19","Nat"],"city":["vizag","east","pd.Nat","vizag"]})
print(a)


# In[4]:


a.dropna()


# In[5]:


a.dropna(axis="columns")


# In[6]:


a.dropna(how="all")


# In[7]:


a.dropna(how="any")


# In[8]:


a.dropna(thresh=2)


# In[9]:


a.dropna(subset=["city"])


# In[16]:


b=a.fillna(0)
print(b)


# In[17]:


a['Name'].str.split(',')


# In[22]:


b=a["city"]=a["city"].str.replace('city','name')
print(b)


# In[ ]:





# In[ ]:




