"""Analyzing College Major vs Salary dataset

This 'script' analyzes a college major vs salary dataset to answer questions such as:
    Which college majors start with the higher/lower salary?
    Which college majors have the highest/lowest mid-career salary?
    Which college majors are the lowest risk?
    Which category of degrees have the highest/lowest salary?

This script requires that 'pandas' be installed within the Python
environment you are running this script in.

"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('day71-data/salaries_by_college_major.csv')
df.head()


# In[7]:


df.info()


# In[15]:


df[df['Starting Median Salary'].isnull()]


# In[46]:


df.isnull().tail()


# In[2]:


df.drop(labels=50, axis=0, inplace=True)


# In[24]:


df.tail()


# In[27]:


mask = df['Starting Median Salary'] == df['Starting Median Salary'].max()
df[mask]


# In[32]:


df.loc[43]


# What college major has the highest mid-career salary? How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience).

# In[39]:


df.head()


# In[37]:


df.loc[df['Mid-Career Median Salary'].idxmax()]


# Which college major has the lowest starting salary and how much do graduates earn after university?

# In[42]:


df.loc[df['Starting Median Salary'].idxmin()]


# Lowest Risk Majors

# In[3]:


df['Mid-Career 90th Percentile Salary'] - df['Mid-Career 10th Percentile Salary']
df.insert(loc=5, column='90th - 10th Percentile', value=df['Mid-Career 90th Percentile Salary'].subtract(df['Mid-Career 10th Percentile Salary']))


# Sorting by the Lowest Spread

# In[61]:


df.sort_values(by='90th - 10th Percentile', ascending=True)[['Undergraduate Major', '90th - 10th Percentile']].head()


# Using the .sort_values() method, can you find the degrees with the highest potential? Find the top 5 degrees with the highest values in the 90th percentile. 

# In[73]:


df.sort_values(by='Mid-Career 90th Percentile Salary', ascending=False)[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()


# Majors with the Greatest Spread in Salaries

# In[74]:


df.sort_values(by='90th - 10th Percentile', ascending=False)[['Undergraduate Major', '90th - 10th Percentile']].head()


# In[4]:


df.head()


# Grouping and Pivoting data with pandas

# In[8]:


df.groupby('Group')


# In[7]:


groups = df.groupby('Group')
groups.count()


# In[12]:


groups.mean()


# In[13]:


pd.options.display.float_format = '{:,.2f}'.format


# In[14]:


groups.mean()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




