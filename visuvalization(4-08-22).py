#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
plt.title("lineplot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
x=np.array([0,5])
y=np.array([0,100])
plt.plot(x,y)
plt.show()


# In[2]:


import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,20,30,40,50]
plt.plot(x,y,marker="*",mec="r",color="g")
plt.show()


# In[3]:


import matplotlib.pyplot as plt
x=[2,4,6,8,10]
y=[10,20,30,40,50]
plt.scatter(x,y)
plt.show()
plt.plot(x,y, markes="0", mec="r")
plt.show()


# In[5]:


import matplotlib.pyplot as plt
x=["a","b","c","d","e"]
y=[25,50,75,100,125]
plt.xlabel("students")
plt.ylabel("marks")
plt.bar(x,y)
plt.show()
plt.barh(x,y)
plt.show()


# In[6]:


a=np.array([25,40,35])
plt.pie(a,labels=["oops","html","wt"])
plt.legend(title="subjects")
plt.show()


# In[ ]:




