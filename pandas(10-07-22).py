#!/usr/bin/env python
# coding: utf-8

# In[3]:


## CREATION OF SERIES FROM SCALAR VALUES
import pandas as pd
a=pd.Series([1,2,3])
print(a)


# In[6]:


import pandas as pd
a=pd.Series(["a","b","l"],index=([1,2,3]))
print(a)


# In[7]:


## creation of series from numpy as arrays
import numpy as np
import pandas as pd
a=np.array([1,2,3])
b=pd.Series(a)
print(b)


# In[9]:


## creation of Series from Dictionary
d={'a':1,'b':2,'c':3}
print(d)
b=pd.Series(d)
print(b)


# In[10]:


## ACESSING ELEMENTS OF A SERIES
import pandas as pd
a=pd.Series(["a","b","c"])
a[2]


# In[11]:


import pandas as pd
b=pd.Series([1,2,3],index=["a","b","c"])
s=b["a"]
print(s)


# In[12]:


d=b[[1,2]]
print(d)


# In[13]:


import pandas as np
a=pd.Series(["lavanya","swathi","teju","mahi","siri"],index=[1,2,3,4,5])
print(a)


# In[16]:


######## ATTRIBUTES OF  A SERIES ############
import pandas as pd
a=pd.Series(["lavanya","swathi"],index=[1,2])
a.empty
print(a)


# In[17]:


######## METHODS OF SERIES ########
import numpy as np
import pandas as pd
a=pd.Series(np.arange(5,10,1))
print(a)


# In[18]:


a.head()


# In[19]:


a.head(3)


# In[20]:


a.count()


# In[21]:


a.tail()


# In[22]:


a.tail(3)


# In[23]:


###### MATHEMATICAL OPERATIONS ##################
import pandas as pd
import numpy as np
a=pd.Series([1,2,3])
b=pd.Series([5,6,7])
print(a+b)


# In[24]:


print(a-b)


# In[25]:


print(a*b)


# In[26]:


print(a/b)


# In[1]:


######## DATAFRAME ###########
import pandas as pd
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.array([9,10,11])
d=pd.DataFrame(a)
print(d)


# In[2]:


import pandas as pd
import numpy as np
dict=[{"lavanya":1,"mahitha":2,"teju":3,"siri":4}]
e=pd.DataFrame(dict)
print(e)


# In[3]:


a=pd.Series([{"lavanya":1,"mahitha":2,"teju":3,"siri":4}])
d=pd.DataFrame(a)
print(d)


# In[4]:


import pandas as pd
dict={'student':["lavanya","mahitha","siri","teju"],'section':["a","b","c","d"],"marks":[100,200,300,400]}
a=pd.DataFrame(dict)
print(a)


# In[9]:


####### OPERATIONS ON ROWS AND COLUMNS IN A DATAFRAME
import pandas as pd
a={'Lavanya': pd.Series([90,91,93],
    index=["MATHS","SCIENCE","HINDI"]),
  'Mahitha':pd.Series([92,81,89],
  index=["MATHS","SCIENCE","HINDI"]),
  'Siri':pd.Series([96,98,94],
    index=["MATHS","SCIENCE","HINDI"]),
  'Teju':pd.Series([90,100,97],
   index=["MATHS","SCIENCE","HINDI"])}

MS=pd.DataFrame(a)
print(MS)


# In[10]:


# ADDING new column
MS['Manasa']=['90','95','96']
print(MS)


# In[11]:


#change data of an entire column to a particular value in a DataFrame
MS["Lavanya"]=93
print(MS)


# In[13]:


# Adding a New Row to a DataFrame
MS.loc['DSP']=['89','86','87','89','84']
print(MS)


# In[15]:


#change the data values of a row to a particular value
MS.loc['SCIENCE']=20
print(MS)


# In[16]:


#we can set all values of a DataFrame to a particular value
MS.loc[:]=90
print(MS)


# In[19]:


#Deleting Rows or Columns from a DataFrame
MS=MS.drop('SCIENCE',axis=0)
print(MS)


# In[21]:


#DELETING A COLUMN
MS=MS.drop(['Manasa'],axis=1)
print(MS)


# In[24]:


#Renaming Row Labels of a DataFrame
a=MS.rename({'MATHS':'SUB1','HINDI':'SUB2','DSP':'SUB3'},axis='index')
print(a)


# In[26]:


b=MS.rename({'Lavanya': 'student1','Mahitha':'student2','Siri':'student3','Teju':'student4'},axis='columns')
print(b)


# In[27]:


#Accessing DataFrames Element through Indexing
import pandas as pd
a={'Lavanya': pd.Series([90,91,93],
    index=["MATHS","SCIENCE","HINDI"]),
  'Mahitha':pd.Series([92,81,89],
  index=["MATHS","SCIENCE","HINDI"]),
  'Siri':pd.Series([96,98,94],
    index=["MATHS","SCIENCE","HINDI"]),
  'Teju':pd.Series([90,100,97],
   index=["MATHS","SCIENCE","HINDI"])}

MS=pd.DataFrame(a)
print(MS)


# In[29]:


b=MS.loc['SCIENCE']
print(b)


# In[31]:


print(MS['Lavanya'])


# In[32]:


### Boolean Indexing
a=MS.loc['MATHS']>90
print(a)








# In[35]:


b=MS.loc['MATHS':'SCIENCE','Lavanya']
print(b)


# In[36]:


b=MS.loc['MATHS':'SCIENCE','Lavanya':'Teju']
print(b)


# In[ ]:




