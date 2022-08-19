#!/usr/bin/env python
# coding: utf-8

# In[1]:


###########LINE PLOT ###########
import matplotlib.pyplot as plt
import numpy as np
plt.title("lineplot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
xpoints=np.array([0,5])
ypoints=np.array([0,100])
plt.plot(xpoints,ypoints)
plt.show()


# In[3]:


import matplotlib.pyplot as plt
xpoints=[2,4,6,8,10]
ypoints=[10,20,30,40,50]
plt.plot(xpoints,ypoints ,marker="s" ,color="red")
plt.show()


# In[6]:


################ SCATTER POINTS ##############
import matplotlib.pyplot as plt
x=["a","b","c","d","e"]
y=[10,20,30,40,50]
xlabel="students"
ylabel="marks"
x_title= "marks of students"
plt.scatter(x,y,marker="*", color="blue")
plt.show()


# In[9]:


import matplotlib.pyplot as plt
y=[3,6,7,4,8]
plt.plot(y, marker="*",mec='r',color="green", linewidth="5")
plt.show()


# In[13]:


######### BAR GRAPH #########
import matplotlib.pyplot as plt
import numpy as np
x=["a","b","c","d","e"]
y=["20","40","60","80","100"]
plt.bar(x,y)
plt.show()


# In[14]:


import matplotlib.pyplot as plt
import numpy as np
x=["a","b","c","d","e"]
y=["20","40","60","80","100"]
plt.barh(x,y)
plt.show()


# In[17]:


############ HISTOGRAM ###################3
import matplotlib.pyplot as plt
import numpy as np
y=[3,5,7,9,11]
plt.hist(y,bins=4)
plt.show()


# In[20]:


a=[1.5,2.0,2.5,3.5,4.0]
plt.hist(a,bins=5)
plt.show()


# In[23]:


#################### pie chart ##################
import matplotlib.pyplot as plt
x=[20,20,20,20,20]
plt.pie(a)
plt.show()


# In[24]:


import matplotlib.pyplot as plt
x=[20,20,20,20,20]
plt.pie(a, labels=["CD","COA","DSP","OR","WT"] )
plt.show()


# In[25]:


import matplotlib.pyplot as plt
x=[20,20,20,20,20]
plt.pie(a, labels=["CD","COA","DSP","OR","WT"] )
plt.legend(title="subjects")
plt.show()


# In[27]:


import matplotlib.pyplot as plt
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(1,2,2)
plt.plot(x,y)


# In[28]:


import matplotlib.pyplot as plt
x=[10,20,30,40,50]
y=[1,2,3,4,5]
plt.scatter(x,y)


# In[30]:


plt.scatter(x,y, c="blue", marker="*")
plt.show()


# In[ ]:





# In[10]:


import matplotlib.pyplot as plt
x=[10,20,30,40,50]
y=[1000,1500,2000,2500,3000]
c=["red","yellow","blue","cyan","green"]
plt.scatter(x,y,   edgecolor="green",linewidth=1, marker="s")
plt.show()


# In[11]:


################## BUBBLE PLOT #####################
import matplotlib.pyplot as plt
import numpy as np
x=np.random.rand(50)
y=np.random.rand(50)
z=np.random.rand(50)
color=np.random.rand(50)
plt.scatter(x,y,s=z*1000, c=color, alpha=0.3)


# In[12]:


################# BOX PLOT ###################
import matplotlib.pyplot as plt
import numpy as np
data=[10,20,30,40,50]
plt.boxplot(data)
plt.show()


# In[14]:


a=[10,20,30,40,50,60]
b=[60,70,80,90,100,120]
c=(a,b)
plt.boxplot(c)
plt.show()


# In[16]:


import pandas as pd
df=pd.DataFrame(np.random.rand(10,5),columns=["a","b","c","d","e"])
plt.boxplot(df)
plt.show()


# In[2]:


#explode
import matplotlib.pyplot  as plt
y=[35,27,15,23]
labels=["oops","dsp","cd","coa"]
explode=[0.1,0,0,0]
plt.pie(y,startangle=90, labels=labels, explode=explode, shadow=True)
plt.show()


# In[ ]:




