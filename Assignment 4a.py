#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np

#import the dataset from CSV
Location = "Anaconda2/gradedata.csv"
df = pd.read_csv(Location)

#create the bin dividers
bins = [0, 60, 70, 80, 90, 100]

#create names for the groups
group_names = ['F', 'D', 'C', 'B', 'A']

#create pass_or_fail
#status = ['Fail', 'Fail', 'Fail','Pass', 'Pass']


# categorize column grades based on bins
df['lettergrade'] = pd.cut(df['grade'], bins, labels = group_names)
df['status'] = np.where(df['grade']>80,'pass', 'fail')


df.head(10)


# In[ ]:




