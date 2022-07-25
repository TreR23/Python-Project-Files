#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


#importing pandas


# In[2]:


df = pd.read_csv(r"C:\Users\trero\OneDrive\Documentos\TrRodriguez\Sleep\sleepscore.csv")


# In[ ]:


#Getting sleep data file. Had to include "r" before filepath to correct for syntax error


# In[3]:


df.head(6)


# In[ ]:


#Getting first six rows to inspect data


# In[4]:


df.dtypes


# In[5]:


df.describe


# In[6]:


df.describe()

#Getting summary statistics


# In[7]:


df['deep_sleep_in_minutes']


# In[8]:


df['resting_heart_rate']


# In[9]:


df[['deep_sleep_in_minutes', 'resting_heart_rate']]

#Comparing deep sleep and resting heart rate


# In[10]:


df[df['resting_heart_rate'] > 100]

#Checking to see if I'm going to die soon. Good news, looks like I'm ok for now! :) 


# In[11]:


df[df['deep_sleep_in_minutes'] > 55]

#The ideal amount of deep sleep for someone who sleeps 7 hours is between 55 and 97 minutes. Checking to see where I fall.


# In[12]:


df[df['deep_sleep_in_minutes'] > 97]


# In[13]:


df[(df['deep_sleep_in_minutes'] > 55) & (df['deep_sleep_in_minutes'] < 97)]


# In[14]:


df[(df['deep_sleep_in_minutes'] > 97) & (df['resting_heart_rate'] < 79)]

#Wondering if there's an ideal range and if so, how often I land in it. 


# In[ ]:




