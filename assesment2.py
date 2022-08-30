#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
from pandas import DataFrame


# In[16]:


dict ={"Name":["Martin_Kelly", "Martin_Kelly"],
      "Age":[22, 22],
      "Location":["Nairobi", "Nairobi"],
      "Profile_pic":["image.jpeg","image.jpeg"]}


# In[17]:


df = pd.DataFrame(dict)


# In[18]:


display(df)


# In[19]:


csv = df.to_csv(assesment2.csv)


# In[ ]:


json = df.to_json(assesment2)


# In[ ]:


df.to_excel(assesment2.xls)

