#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a=np.array([1,2,3,4,5])
print(a)


# In[2]:


print(np.__version__)


# In[3]:


print(type(a))


# In[4]:


a=np.array([1,2,3])
print(a)


# In[6]:


b=np.array([[1,2,3],[4,5,6]])
print(b)


# In[7]:


c=np.array([[1,2,3],[4,5,6],[7,0,7]])
print(c)


# In[8]:


print(a.ndim)


# In[9]:


print(b.ndim)


# In[10]:


print(c.ndim)


# In[13]:


## Higher dimensional arrays ###
a = np.array([1,2,3], ndim=5)
print(a)


# In[14]:


## numpy array indexing ##
import numpy as np
a=np.array([1,2,3])
print(a[0])


# In[15]:


b=np.array([4,5,6])
print(a[0]+b[2])


# In[16]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a[1,2])


# In[17]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a[0,-1])


# In[18]:


import numpy as np
c=np.array([6,7,8])
print(c[1:3])


# In[19]:


import numpy as np
a=np.array([1,2,3])
print(a[0:])


# In[20]:


print(a[:1])


# In[21]:


print(a[-3:-1])


# In[22]:


import numpy as np
a=np.array([1,2,3,4,5])
print(a[0:2:4])


# In[26]:


print([0::1])


# In[29]:


import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a[1,1:4])


# In[31]:


print(a[0,1:3])


# In[32]:


print(a[0:1,2:3])


# In[33]:


##checking the datatypes of an array
import numpy as np
b=np.array([11,12,13,14,15])
print(b.dtype)


# In[34]:


c=np.array(["lavanya","swathi"])
print(b.dtype)


# In[36]:


b=np.array([11,12,13,14],dtype='s')
print(b)
print(b.dtype)


# In[37]:


# numpy array copy vs view
import numpy as np
b=np.array([1,2,3])
x=b.copy()
b[0]=36
print(b)
print(x)


# In[38]:


x=b.view()
b[0]=36
print(b)
print(x)


# In[39]:


## check if array owns its data
import numpy as np
b=np.array([1,2,3])
x=b.copy()
y=b.view()
b[0]=36
print(x)
print(y)


# In[40]:


import numpy as np
b=np.array([1,2,3])
print(b.shape)


# In[43]:


b=np.array([1,2,3],ndim=5)
print(b)
print(b.shape)


# In[47]:


import numpy as np
b=np.array([1,2,3],ndmin=5)
print(b)
print(b.shape)


# In[48]:


import numpy as np
b=np.array([1,2,3,4,5,6,7,8,9,0,11,12])
print(b.reshape(3,4))


# In[49]:


print(b.reshape(4,3))


# In[52]:


print(b.reshape(2,3,2))


# In[53]:


###NUMPY ARRAY,ITERATIING
import numpy as np
b=np.array([1,2,3])
for x in b:
    print(x)


# In[54]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
 for x in a:
        for y in x:
            for z in y:
                print(z)
            


# In[56]:


import numpy as np
b=np.array([[1,2,3],[4,5,6]])
for x in np.nditer(b):
    print(x)


# In[57]:


### JOINING NUMPY ARRAYS
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.concatenate((a,b))
print(c)


# In[58]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[5,6,7],[8,9,10]])
c=np.concatenate((a,b),axis=1)
print(c)


# In[59]:


c=np.stack((a,b),axis=1)
print(c)


# In[60]:


import numpy as np
b=np.array([1,2,3])
c=np.array([4,5,6])
d=np.stack((b,c))
print(d)


# In[61]:


d=np.stack((b,c))
print(d)


# In[62]:


d=np.dstack((b,c))
print(d)


# In[63]:


# Numpy splitting array
import numpy as np
a=np.array([1,2,3])
b=np.array_split(a,3)
print(b)


# In[64]:


import numpy as np
x=np.array([1,2,3])
y=np.array([4,5,6])
print(np.add(x,y))


# In[65]:


np.all(x)


# In[ ]:




