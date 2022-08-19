#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#################1st unit########################


# In[1]:


#VARIABLES IN PYTHON#########
a=5
b=8
print(a,b)


# In[2]:


1b="yogi"
print(1b)


# In[ ]:


###########################################STRING OPERATIONS################################################


# In[5]:


a="LAVANYA"
b=a.lower()
print(b)


# In[7]:


b=a.upper()
print(b)


# In[9]:


c=a.title()
print(c)


# In[10]:


d=a.capitalize()
print(d)


# In[12]:


s=" lavanya "
a=s.center(20)
print(a)


# In[14]:


a="hi i am lavanya, am i a student"
b=a.count("am")
print(b)


# In[15]:


a="he is yogi"
b=a.encode()
print(b)


# In[16]:


a="lavanya"
b=a.endswith(".")
print(b)


# In[19]:


a="l\ta\tva\tnya"
b=a.expandtabs(6)
print(b)


# In[2]:


a="lavanya,jayanthi, swathi, yogi"
b=a.find("yogi")
print(b)


# In[1]:


b=a.index("yogi")


# In[24]:


b=a.format()
print(b)


# In[26]:


b=a.format_map("lavanya")
print(b)


# In[28]:


a="lavanya, mahitha,siri,teju"
b=a.index("teju")
print(b)


# In[30]:


b=a.isalnum()
print(b)


# In[32]:


a="lavanya"
b=a.isalpha()
print(b)


# In[33]:


b=a.isdecimal()
print(b)


# In[34]:


b=a.isdigit()
print(b)


# In[35]:


b=a.isidentifier()
print(b)


# In[36]:


b=a.islower()
print(b)


# In[37]:


b=a.isprintable()
print(b)


# In[38]:


b=a.isspace()
print(b)


# In[39]:


b=a.istitle()
print(b)


# In[40]:


b=a.isupper()
print(b)


# In[41]:


s="lavanya","mahitha"
x="#".join(s)
print(x)


# In[43]:


x="lavanya"
b=x.ljust(20)
print(b," is a student")


# In[3]:


a="apple"
b=a.ljust(40)
print(b,"is a fruit")


# In[47]:


x="lavanya"
y=x.maketrans("l","p")
print(x.translate(y))


# In[49]:


x="section e girls"
y=x.partition("girls")
print(y)


# In[52]:


a="i am lavanya"
b=a.replace("lavanya","girl")
print(b)


# In[54]:


a=" hi this is lavanya"
b=a.rfind("is")
print(b)


# In[58]:


b=a.rjust(30)
print(b,"hi ")


# In[59]:


a="lavanya,mahitha,siri,teju"
b=a.rsplit(",")
print(b)


# In[60]:


a="Hello LAvanya"
b=a.swapcase()
print(b)


# In[61]:


a="30"
b=a.zfill(10)
print(b)


# In[62]:


a="hello"
b=a.zfill(20)
print(b)


# In[63]:


########################LIST############################
a=[1,2,"lavanya"]
print(a)
print(type(a))


# In[64]:


print(len(a))


# In[65]:


b=a.index(2)
print(b)


# In[66]:


c=a[-1]
print(c)


# In[67]:


a=[1,2,3,4]
print(a[:3])


# In[68]:


print(a[1:])


# In[69]:


print(a[0:])


# In[71]:


a.pop(3)


# In[72]:


print(a)


# In[77]:


b=[4]
print(a+b)


# In[79]:


c=max(a)
print(c)


# In[81]:


d=min(a)
print(d)


# In[82]:


c=[180615,180122]
f=a.extend(c)
print(f)


# In[83]:


d=a.count(2)
print(d)


# In[86]:


s=[1,2,3,4,5,6,7,8]
s.reverse()
print(s)


# In[87]:


s.append(9)
print(s)


# In[88]:


s.clear()
print(s)


# In[90]:


s=[1,2,3,4,5,6,7,8,9,10]
a=len(s)
print(a)


# In[92]:


g=sum(s)
print(g)


# In[94]:


f=[67,23,4,5,2,6,7,9]
sorted(f)


# In[96]:


del(f[-1])
print(f)


# In[ ]:


#################################TUPLE###############################


# In[ ]:





# In[ ]:





# In[98]:


a=(5,6,7,8)
print(a)
print(type(a))


# In[99]:


a.append(9)
print(a)


# In[100]:


s=list(a)
s.append(9)
d=tuple(s)
print(d)


# In[101]:


print(s)


# In[102]:


a.count(5)


# In[104]:


a=(1,2,3,5)
b=(6,7,8,9)
a=a+(b)
print(a)


# In[106]:


s=(9,10,11)
(m,l,r)=s
print(m,l,r)


# In[111]:


(m,*l)=s
print(m,l)


# In[113]:


(*m,l)=s
print(m,l)


# In[116]:


a=[1,2,3,4]
t1=('a','b','c','d')
x=list(t1)
b=a+x
print(b)


# In[117]:


len(b)


# In[119]:


d=b.(a)
print(d)


# In[ ]:


###########################DICTIONARY################################


# In[1]:


Dict={1:"one",2:"two",3:"three"}
print(Dict)


# In[2]:


Dict={}
Dict[1]="one"
Dict[2]="two"
Dict[3]="three"
Dict[4]="four"
print(Dict)


# In[3]:


print(type(Dict))


# In[4]:


Dict["5"]="five"
print(Dict)


# In[5]:


len(Dict)


# In[6]:


Dict.pop(3)


# In[7]:


print(Dict)


# In[8]:


Dict[3]="three"
print(Dict)


# In[14]:


a=Dict.keys()
print(a)


# In[15]:


b=Dict.values()
print(b)


# In[16]:


c=Dict.items()
print(c)


# In[18]:


Dict.update({6:"six"})
print(Dict)


# In[20]:


s=Dict.popitem()
print(s)


# In[21]:


Dict.setdefault(3,"three")


# In[22]:


a=all(Dict)
print(a)


# In[23]:


b=any(Dict)
print(b)


# In[26]:


c=sorted(Dict)
print(c)


# In[ ]:


############################### SET OPERATIONS ###############################


# In[27]:


a={1,2,3}
b={3,4,5,6}
print(a,b)



# In[29]:


print(type(a))


# In[30]:


a.union(b)


# In[31]:


a.intersection(b)


# In[35]:


s=a.difference(b)
print(s)


# In[38]:


b.discard(5)
print(b)


# In[39]:


a.issubset(b)

b.issubset(a)
# In[40]:


b.issubset(a)


# In[41]:


a={1,2,3,4,5,6}
b={3,4,5,6,7,8,9}
a.issubset(b)


# In[42]:


b.issubset(a)


# In[43]:


a.add(10)
print(a)


# In[44]:


a.remove(2)
print(a)


# In[46]:


e={1,2}
f={3}
e.isdisjoint(f)


# In[47]:


a.intersection_update(b)
print(a)


# In[48]:


a.issuperset(b)


# In[49]:


b.issuperset(a)


# In[51]:


d=a.symmetric_difference(b)
print(d)
                         


# In[54]:


z=a.symmetric_difference_update(b)
print(z)


# In[ ]:




