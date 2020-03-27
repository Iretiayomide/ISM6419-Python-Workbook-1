#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
#create dataset
names = ['Bob','Jessica','Mary','John','Mel','Jane', 'Tina']
grades = [76,-2,77,78,101,-5,-3]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,columns=['Names', 'Grades'])

#replace the grades that are less than 0
df.loc[(df['Grades'] <= 0,'Grades')] = 0

#view new dataset
df

