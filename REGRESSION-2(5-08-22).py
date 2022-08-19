#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
x=np.array([5,15,25,35,45,55]).reshape(-1,1)
print(x)
y=np.array([5,20,14,32,22,38])
print(y)
plt.scatter(x,y)


# 

# In[2]:


model=LinearRegression()
model.fit(x,y)
print(model.intercept_)
print(model.coef_)
print(model.score(x,y))
y_pred=model.predict(x)
print(y_pred)
print(model.score(x,y_pred))
plt.scatter(x,y)
plt.plot(x,y_pred,color="yellow",marker="*",mec="g")


# In[11]:


################## MULTILINEAR REGRESSION ###################
import numpy as np
from sklearn.linear_model import LinearRegression
x=[[0,1],[5,1],[15,2],[25,5],[35,11],[45,15],[55,34],[60,35]]
y=[4,5,20,14,32,22,38,43]
x,y=np.array(x),np.array(y)
model=LinearRegression().fit(x,y)
r_sq=model.score(x,y)
print(f"coefficient of determination:{r_sq}")
print(f"intercept:{model.intercept_}")
print(f"coefficients:{model.coef_}")
y_pred=model.predict(x)
print(f"predicted response:/n {y_pred}")
y_pred=model.intercept_ +np.sum(model.coef_*x, axis=1)
print(f"predicted response:/n {y_pred}")
x_new=np.arange(10).reshape((-1,2))
y_new=model.predict(x_new)


# In[9]:


from sklearn.preprocessing import polynomial Featuers
import numpy as np
x=np.array([5,15,25,35,45,55]).reshape((-1,1))
y=np.array([5,11,2,8,25,32])
transformer=polynomialFeatuers(degree=2,include_bias=False)
transformerfit(x)
x=transformer.transform(x)
from sklearn.linear_model import Linear Regression
model=LinearRegression().fit(x,y)
r_sq=model.score(x,y)
print("r square",r_sq)
print("intercept:",model.intercept_)
print("coef:",model.coef_)


# In[ ]:





# In[ ]:





# In[ ]:




