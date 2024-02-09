#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 第三方套件 yfinance, 可用來串接 Yahoo Finance API 下載股票的價量資訊. 而且拿到的資料就是 Pandas 的 DataFrame
import yfinance as yf
import pandas as pd
import csv


# In[2]:


# 時間範圍為2022/01-2022/12 2330為台積電
df = yf.download("2330.TW", start = '2022-01-01', end = '2022-12-31')
df


# In[3]:


# 只保留收盤價
df = df[['Close']]
df


# In[4]:


# 計算每日報酬率
df['Daily_Return'] = (df['Close'].shift(0) - df['Close'].shift(1)) / df['Close'].shift(1) * 100

# 將第一天設為 0
df['Daily_Return'] = df['Daily_Return'].fillna(0)
df


# In[5]:


# 只保留 daily return
df = df[['Daily_Return']]
df


# In[6]:


# 查看所有的daily return
pd.set_option('display.max_rows', None)
df


# In[7]:


# 轉成 csv 檔
df.to_csv('Daily_Return.csv', encoding='utf-8')

