#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("c.csv")
print(df)


# In[16]:


c


# In[19]:


import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("s.csv")
profitlist=df['total profits'].tolist()
monthlist=df['month number'].tolist()
plt.plot(monthlist,profitlist,label='profit of last year',color='r',marker='o',markerfacecolor='blue',linestyle="--",linewidth=3)
plt.xlabel('month number')
plt.ylabel('profit in dollar')
plt.xticks(monthlist)
plt.title("company profit per month")
plt.yticks([10,20,30,40,50,60,70,80,90,110,120])

plt.plot([1,2,3,4,5,6,7],[10000,20343,10340,12900,12456,23456,34562])

plt.show()




# In[30]:


# read face cream sales data of each month and show it using a scatter plot
import pandas  as pd
import matplotlib.pyplot as plt
df=pd.read_csv("s.csv")
plt.scatter(monthlist,shampoo, label="face cream sales data")
plt.xlabel=('month number')
plt.ylabel=("total units")
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],[20,21,23,23,21,24,25,26,24,21,34,34])
plt.show()


# In[ ]:







