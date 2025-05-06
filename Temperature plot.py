#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import plotly.graph_objects as go
# Fetch the data.
df = pd.read_csv("https://ourworldindata.org/grapher/temperature-anomaly.csv?v=1&csvType=full&useColumnShortNames=true", storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'})

# Fetch the metadata
metadata = requests.get("https://ourworldindata.org/grapher/temperature-anomaly.metadata.json?v=1&csvType=full&useColumnShortNames=true").json()
df.info()
df.head()


# In[59]:


#Lets drop the NAN from the "code" column
df.dropna(inplace= True)
df.head()
df.info()


# In[60]:


df["near_surface_temperature_anomaly"].describe()


# In[95]:


#lets extract specific column from our data frame(df) and assign it to respective variables

x= df["Year"]
y= df["near_surface_temperature_anomaly"]
z=df["near_surface_temperature_anomaly_lower"]
s=df["near_surface_temperature_anomaly_upper"]

#Now create a figure 
plt.figure(figsize=(13, 6))
plt.plot(x,s,color="gray",label= 'upperbound')
plt.plot(x,z,color="blue",label="lowerbound")
plt.plot(x,y,color="red", label='average')

#label the x and y axis

plt.xlabel("Year", fontsize=12, labelpad=5)
plt.ylabel("Temperature in °C", fontsize=12, labelpad=5)
plt.title("Global Near-Surface Temperature Anomalies (Yearly Trends)")
plt.ylim(-0.5 , 2)

# Add grid and legend
plt.grid(True, linestyle="--", alpha=0.75)
plt.legend()
plt.show()


# In[93]:


p_correlation= df["Year"].corr(df["near_surface_temperature_anomaly"])
p_correlation

