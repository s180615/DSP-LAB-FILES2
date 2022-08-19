#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
negative_corr={'Hours_Work_before_Training':[10,9,8,7,6,5,4,3,2,1], 'calorie_burnage':[220,240,260,280,300,320,340,360,380,400]}
negative_corr=pd.DataFrame(data=negative_corr)
x=negative_corr['Hours_Work_before_Training']
y=negative_corr['calorie_burnage']
plt.plot(x,y)
plt.show()


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
positive_corr={'Hours_Work_before_Training':[1,2,3,4,5,6,7,8,9,10], 'calorie_burnage':[220,240,260,280,300,320,340,360,380,400]}
positive_corr=pd.DataFrame(data=negative_corr)
x=positive_corr['Hours_Work_before_Training']
y=positive_corr['calorie_burnage']
plt.plot(x,y)
plt.show()


# In[ ]:




