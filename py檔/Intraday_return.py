#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 第三方套件 yfinance, 可用來串接 Yahoo Finance API 下載股票的價量資訊. 而且拿到的資料就是 Pandas 的 DataFrame
import yfinance as yf
import pandas as pd
import csv
import sys


# In[21]:

# Download intraday data for 2330.TW
data = yf.download("2330.TW", start="2022-01-01", end="2023-06-30", interval="1d")


# In[22]:


# Calculate intraday returns
data["Intraday_Return"] = (data["Close"] - data["Open"]) / data["Open"] * 100


# In[23]:


# Save the intraday return data to a CSV file
data.to_csv('Intraday return/2330_Intraday_Return.csv', encoding='utf-8')


# In[24]:


all = data["Intraday_Return"].sum()
print(all)


# In[25]:


# Download intraday data for 2412.TW
data2 = yf.download("2412.TW", start="2022-01-01", end="2023-06-30", interval="1d")


# In[26]:


# Calculate intraday returns
data2["Intraday_Return"] = (data2["Close"] - data2["Open"]) / data2["Open"] * 100


# In[27]:


# Save the intraday return data to a CSV file
data2.to_csv('Intraday return/2412_Intraday_Return.csv', encoding='utf-8')


# In[28]:


all = data2["Intraday_Return"].sum()
print(all)


# In[34]:


# Download intraday data for 1795.TW
data3 = yf.download("1795.TW", start="2022-01-01", end="2023-06-30", interval="1d")


# In[35]:


# Calculate intraday returns
data3["Intraday_Return"] = (data3["Close"] - data3["Open"]) / data3["Open"] * 100


# In[36]:


# Save the intraday return data to a CSV file
data3.to_csv('Intraday return/1795_Intraday_Return.csv', encoding='utf-8')


# In[37]:


all = data3["Intraday_Return"].sum()
print(all)


# In[ ]:




