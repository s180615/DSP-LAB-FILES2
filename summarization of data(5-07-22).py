#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
p1=pd.Series([1,2,3,4,5,5])
p2=pd.Series([1,2,2,3,40,5])
p3=pd.Series([1,20,3,3,4,5])
p4=pd.Series([1,20,3,4,5])
p5=pd.Series([1,2,2,30,4,5])
p6=pd.Series([1,25,3,4,4,5])
p7=pd.Series([1,2,39,4,5,5])
p8=pd.Series([1,24,3,3,54,5])
p9=pd.Series([1,20,3,4,5,5])
p10=pd.Series([1,2,3,3,48,5])


# In[4]:


p1.describe()


# In[5]:


p2.describe()


# In[6]:


p3.describe()


# In[7]:


p4.describe()


# In[8]:


p5.describe()


# In[9]:


p6.describe()


# In[10]:


p7.describe()


# In[11]:


p8.describe()


# In[12]:


p9.describe()


# In[13]:


p10.describe()


# In[16]:


p1.mean(),p2.mean(),p3.mean(),p4.mean(),p5.mean(),p6.mean(),p7.mean(),p8.mean(),p9.mean(),p10.mean()


# In[17]:


p1.median(),p1.median(),p2.median(),p3.median(),p4.median(),p5.median(),p6.median(),p7.median(),p8.median(),p9.median(),p10.median()


# In[18]:


p1.mode(),p2.mode(),p3.mode(),p4.mode(),p5.mode(),p6.mode(),p7.mode(),p8.mode(),p9.mode(),p10.mode()


# In[20]:


p1.var(),p2.var(),p3.var(),p4.var(),p5.var(),p6.var(),p7.var(),p8.var(),p9.var(),p10.var()


# In[22]:


p1.std(),p2.std(),p3.std(),p4.std(),p5.std(),p6.std(),p7.std(),p8.std(),p9.std(),p10.std()


# In[27]:


import matplotlib.pyplot as plt
population=['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10']
mean=[3.3333333333333335,8.833333333333334,6.0, 6.6,7.333333333333333,7.0,9.333333333333334,15.0,6.333333333333333,10.333333333333334]
plt.bar(population,mean)
plt.title('mean of the popualtion')
plt.xlabel('population')
plt.ylabel('mean')
plt.bar(mean)
plt.show()


# In[32]:


import matplotlib.pyplot as plt
population=['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10']
mean=[3.3333333333333335,8.833333333333334,6.0, 6.6,7.333333333333333,7.0,9.333333333333334,15.0,6.333333333333333,10.333333333333334]
plt.hist(mean,bins=10)
plt.title('mean of the popualtion')
plt.xlabel('population')
plt.ylabel('mean')

plt.show()


# 

# In[35]:


import matplotlib.pyplot as plt
population=['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10']
median=[3.5, 3.5, 2.5, 3.5, 4.0, 3.0, 4.0, 4.5, 4.0, 4.5]
plt.bar(population,median)
plt.title('median of the popualtion')
plt.xlabel('population')
plt.ylabel('median')
plt.show()


# In[36]:


import matplotlib.pyplot as plt
population=['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10']
mode=['5','2','3','2','5','3','4','3','5','3']
plt.bar(population,mode)
plt.title('mode of the popualtion')
plt.xlabel('population')
plt.ylabel('mode')
plt.show()


# In[44]:


import matplotlib.pyplot as plt
mean=3.333333
std =1.632993
minimum =1.000000
fq = 2.250000
sq= 3.500000
tq= 4.750000
maximum=5.000000
variance=2.666666666666667
mode=5
parameters=[mean,std,minimum,fq,sq,tq,maximum,variance,mode]
population=['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10']
plt.hist(parameters,bins=30)
plt.xlabel("parameters")
plt.ylabel("population")
plt.show()


# In[70]:


import numpy as np
import matplotlib.pyplot as plt
mean=3.333333
std =1.632993
minimum =1.000000
fq = 2.250000
sq= 3.500000
tq= 4.750000
maximum=5.000000
variance=2.666666666666667
mode=5
parameters=np.array([mean,std,minimum,fq,sq,tq,maximum,variance,mode])
plt.legend(title="population one analysis")


plt.pie(parameters,labels=(['mean','std','minimum','fq','sq','tq','maximum','variance','mode']))

plt.show()
plt.hist(parameters,bins=30)
plt.show()


# In[60]:


import numpy as np
import matplotlib.pyplot as plt
mean =     8.833333
std   =   15.328622
minimum=       1.000000
fq=       2.000000
sq=       2.500000
tq=       4.500000
maximum=      40.000000

variance=234.99
mode=2
parameters=np.array([mean,std,minimum,fq,sq,tq,maximum,variance,mode])
plt.legend(title="population one analysis")


plt.pie(parameters,labels=(['mean','std','minimum','fq','sq','tq','maximum','variance','mode']))

plt.show()
plt.hist(parameters,bins=30)
plt.show()


# In[59]:


import numpy as np
import matplotlib.pyplot as plt

mean  =    6.0000
std    =   6.9857
minimum=       1.0000
fq=       3.0000
sq=      3.5000
tq=      4.7500
maximum=      20.0000
variance=234.99
mode=2
parameters=np.array([mean,std,minimum,fq,sq,tq,maximum,variance,mode])
plt.legend(title="population one analysis")



plt.pie(parameters,labels=(['mean','std','minimum','fq','sq','tq','maximum','variance','mode']))


plt.show()
plt.hist(parameters,bins=30)
plt.show()


# In[61]:


import numpy as np
import matplotlib.pyplot as plt


parameters=np.array([mean,std,minimum,fq,sq,tq,maximum,variance,mode])
plt.legend(title="population one analysis")


mean  =    6.600000
std   =    7.635444
minimum=       1.000000
fq=      3.000000
sq=       4.000000
tq=       5.000000
maximum=      20.000000
variance=58.3
mode=2
plt.pie(parameters,labels=(['mean','std','minimum','fq','sq','tq','maximum','variance','mode']))


plt.show()
plt.hist(parameters,bins=30)
plt.show()


# In[62]:


import numpy as np
import matplotlib.pyplot as plt
mean    =  7.333333
std   =   11.201190
minimum=       1.000000
fq=       2.000000
sq=       3.000000
tq=      4.750000
maximum=      30.000000

variance=43.8
mode=4
parameters=np.array([mean,std,minimum,fq,sq,tq,maximum,variance,mode])
plt.legend(title="population one analysis")



plt.pie(parameters,labels=(['mean','std','minimum','fq','sq','tq','maximum','variance','mode']))


plt.show()
plt.hist(parameters,bins=30)
plt.show()


# In[79]:


import matplotlib.pyplot as plt
import numpy as np
population=['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10']
data=(3.3333333333333335,
 8.833333333333334,
 6.0,
 6.6,
 7.333333333333333,
 7.0,
 9.333333333333334,
 15.0,
 6.333333333333333,
 10.333333333333334)
plt.legend(title="population mean analysis")

plt.pie(data,labels=['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10'])
plt.show()
plt.hist(population,30)
pd.cut(population)
plt.show()


# In[78]:


import matplotlib.pyplot as plt
import numpy as np
population=['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10']
median=(3.5, 3.5, 2.5, 3.5, 4.0, 3.0, 4.0, 4.5, 4.0, 4.5)
plt.legend(title="population median analysis")

plt.pie(median,labels=['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10'])
plt.show()
plt.hist(population,30)
plt.show()


# In[2]:





# In[ ]:




