#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


df = pd.read_csv("insurance_data.csv")
df.head()


# In[7]:


plt.scatter(df.age,df.bought_insurance,marker='+',color='red')


# In[8]:


from sklearn.model_selection import train_test_split


# In[10]:


X_train, X_test, y_train, y_test = train_test_split(df[['age']],df.bought_insurance,train_size=0.8)


# In[11]:


X_test


# In[12]:


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()


# In[13]:


model.fit(X_train, y_train)


# In[14]:


X_test


# In[1]:


y_predicted = model.predict(X_test)


# In[15]:


model.predict_proba(X_test)


# In[16]:


model.score(X_test,y_test)


# In[ ]:





# In[19]:


X_test


# In[20]:


model.coef_


# In[21]:


model.intercept_


# In[ ]:


import math
def sigmoid(x):
  return 1 / (1 + math.exp(-x))


# In[ ]:


def prediction_function(age):
    z = 0.042 * age - 1.53 # 0.04150133 ~ 0.042 and -1.52726963 ~ -1.53
    y = sigmoid(z)
    return y


# In[ ]:





# In[ ]:





# In[ ]:




