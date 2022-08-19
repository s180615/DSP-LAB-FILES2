#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import urllib.request
import re
import be
url="https://theuselessweb.com/"
page=urllib.request.urlopen(url)
html_page=page.read()
html=html_page.decode("utf-8")
print(html)
x=re.findall("<h1>",html)
print(x)


# In[2]:


import pandas as pd
import urllib.request
import re
url="https://theuselessweb.com/"
page=urllib.request.urlopen(url)
html_page=page.read()
html=html_page.decode("utf-8")
print(html)
x=re.findall("(['img'])",html)
print(x)


# In[3]:


import pandas as pd
import urllib.request
import re
url="https://theuselessweb.com/"
page=urllib.request.urlopen(url)
html_page=page.read()
html=html_page.decode("utf-8")
print(html)
x=re.findall("(['href'])",html)
print(x)


# In[4]:


import pandas as pd
import urllib.request
import re
url="https://theuselessweb.com/"
page=urllib.request.urlopen(url)
html_page=page.read()
html=html_page.decode("utf-8")
print(html)
x=re.findall("(['h'])",html)
print(x)


# In[ ]:




