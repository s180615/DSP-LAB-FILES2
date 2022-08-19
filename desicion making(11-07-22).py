#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df=pd.read_csv("salaries.csv.csv")
print(df)


# In[4]:


a=df.head()
print(a)


# In[9]:


a=df.drop("salary_more_then_100k", axis=1)
print(a)


# In[11]:


from sklearn.preprocessing import Labelerror
le_company=LabelEncoder()
le_job=LabelEncoder()
le_degree=LabelEncoder()


# In[ ]:


inputs["company_n"]

