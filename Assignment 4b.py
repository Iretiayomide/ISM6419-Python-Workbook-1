#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np

#import the dataset from CSV
Location = "Anaconda2/gradedata.csv"
df = pd.read_csv(Location)

#create timemgt column
df['timemgt'] = np.where((df['exercise']>3) & (df['hours']>17),'busy', 'not busy')

df.head(10)


# In[ ]:




