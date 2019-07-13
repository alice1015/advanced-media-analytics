#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import scipy


# In[7]:


raw = pd.read_csv('dcm_advertiser8548780_8548005_activity_20190712_20190713_045944_2591391421.csv.gz', compression='gzip', header=0, sep=',', error_bad_lines = False)
raw.head(5)


# In[13]:


raw_needed_columns = pd.DataFrame([raw['Event Time'], raw['Interaction Time'], raw['Campaign ID'], raw['Event Sub-Type']])
raw_needed_columns.head(5)


# In[14]:


columns = pd.DataFrame.transpose(raw_needed_columns)


# In[15]:


columns.head(5)


# In[18]:


be_campaign = columns['Campaign ID'] == 21205932
uk_campaign = columns['Campaign ID'] == 21493381


# In[51]:


be_only = columns[be_campaign]


# In[52]:


len(be_only)


# In[53]:


uk_only = columns[uk_campaign]


# In[54]:


len(uk_only)


# In[56]:


be_uk = pd.concat([be_only, uk_only])


# In[57]:


be_uk.head(5)


# In[58]:


len(be_uk)


# In[66]:


event_time = pd.to_datetime(be_uk['Event Time'], unit = 'us')
interaction_time = pd.to_datetime(be_uk['Interaction Time'], unit = 'us')


# In[68]:


event_time.head(5)


# In[69]:


time_lag = event_time - interaction_time


# In[70]:


time_lag.head(5)


# In[78]:


time_lag_seconds = time_lag / np.timedelta64(1,'s')


# In[85]:


campaign_id = be_uk["Campaign ID"]


# In[86]:


event_sub_type = be_uk["Event Sub-Type"]


# In[87]:


be_uk_new = pd.DataFrame([event_time, interaction_time, campaign_id,  time_lag_seconds, event_sub_type])


# In[88]:


be_uk_new.head(5)


# In[89]:


be_uk_ready = pd.DataFrame.transpose(be_uk_new)


# In[90]:


be_uk_ready.head(5)


# In[100]:


be_uk_ready.columns = ['event_time','interaction_time','campaign_id','time_lag','event_sub-type']


# In[103]:


be_uk_ready.columns


# In[104]:


be_uk_ready.head(5)


# In[106]:


be_uk_ready.to_csv('be_uk.csv',index=False)


# In[ ]:




