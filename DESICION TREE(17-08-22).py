#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
df=pd.read_csv("salaries.csv.csv")
train=df[["company","job","degree"]]
target=df["salary_more_then_100k"]
from sklearn.preprocessing import LabelEncoder
le_company=LabelEncoder()
le_job=LabelEncoder()
le_degree=LabelEncoder()
df["company_n"]=le_company.fit_transform(df["company"])
df["job_n"]=le_job.fit_transform(df["job"])
df["degree_n"]=le_degree.fit_transform(df["degree"])
new=df[["company_n","job_n","degree_n"]]
from sklearn import tree
model=tree.DecisionTreeClassifier()
model.fit(new,target)
model.score(new,target)
model.predict([[1,0,0]])


# In[7]:


import pandas as pd
df=pd.read_csv("salaries.csv.csv")
print(df)


# In[ ]:





# In[ ]:





# In[ ]:




