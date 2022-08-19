#!/usr/bin/env python
# coding: utf-8

# In[ ]:


######################## CONDITIONS AND BRANCHING LOOPS ################################


# In[1]:


# if statement
a=35
b=200
if b>a:
    print("b is greater than a")


# In[2]:


#Elif statement
a=55
b=55
if a>b:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")


# In[5]:


##Else statement
a=100
b=299
if a>b:
    print("a is greater than b")
elif b==a:
    print("b is equal to  a")
else:
    print("b is greater than a")


# In[11]:


#####   Nested if statement
x=32
if x>10:
    print("x is greater than 10")
    if (x<10):
        print("x is less than 10")
else:
        print("x is equal to 10")
        


# In[12]:


##pass statement(avoiding error)
a=100
b=300
if a>b:
    pass


# In[13]:


#############looping statements ##########
###### for loop ##########
a=[1,2,3,4,5]
for x in a:
    print(x)


# In[15]:


a=["banana","apple","orange"]
for x in "banana":
    print(x)


# In[33]:


for x in a:
    print(x)
    if (x=="apple"):
        break
            
    
 


# In[34]:


a=["lavanya","mahitha","siri","teju"]
for x in a:
     if (x=="siri"):
            continue
print(x)
        
    


# In[35]:


for x in range(10):
    print(x)


# In[39]:


for x in range(2,7):
    print(x)


# In[44]:


for x in range(2,20,2):
    print(x)


# In[46]:


a=["mahitha","siri","lavanya","teju"]
b=["b1","b2","b3","b4"]
for x in a:
    for y in b:
        print(x,y)


# In[ ]:


i=1
while(i<6):
    print(i)
    if i==3:
        break
    i=i+1


# In[ ]:


################## lab record ###########################


# In[ ]:


# PROGRAM TO FIND GREATEST NUMBER AMONG 3 NUMBERS USING IF CONDITION


# In[ ]:


a=int(input("enter a number=))
b=int(input("enter a number=))
c=int(input("enter a number=))
if a>b & a>c:
            print(" a is greatest number")
if b>a & b>c:
            print("b is greatest number")
if c>a & c>b:
            print("c is greatest number")
            


# In[ ]:





# In[ ]:




