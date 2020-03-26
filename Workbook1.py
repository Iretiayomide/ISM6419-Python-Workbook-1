#!/usr/bin/env python
# coding: utf-8

# In[1]:


print "Hello, World"


# In[5]:


import pandas as pd
Location = "Anaconda2/state.csv"
df = pd.read_csv(Location)


# In[6]:


df.head()

