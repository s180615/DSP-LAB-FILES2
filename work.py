#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
x=[2,4,5,1,5,7,4,4,8]
y=[23,34,12,34,45,23,67,34,54]
color=["r","b","pink","black","green","white","yellow","red","blue"]
size=[110,123,134,145,156,134,123,134,145]
plt.scatter(x,y,marker="^",c=color,s=size,edgecolor="black",linewidth=2)
plt.show()


# In[4]:


import numpy as n
print(n.random.random(40))


# In[7]:


x=n.random.random(40)
y=n.random.random(40)
z=n.random.random(40)
color=["red","green","yellow","black","blue",
      "red","green","yellow","black","blue",
      "red","green","yellow","black","blue",
      "red","green","yellow","black","blue"
      ,"red","green","yellow","black","blue",
      "red","green","yellow","black","blue",
      "red","green","yellow","black","blue",
      "red","green","yellow","black","blue"]
plt.scatter(x,y,z*500,marker="<",alpha=0.3,c=color)


# In[2]:


import pandas as pd
import numpy as np
df=pd.read_csv("sl.csv")
print(df)


# In[3]:


print(df.groupby(["GENDER"]).mean())


# In[4]:


a=df.groupby(["GENDER","DEPT"])
print(a)


# In[5]:


print(df.groupby(["GENDER"]))


# In[6]:


print(a.groups)


# In[10]:


print(df.groupby(["DEPT"]).mean())


# In[14]:


print(df.groupby(["DEPT"]).max())


# In[15]:


print(df.groupby(["GENDER"]).max())


# In[ ]:


print()

