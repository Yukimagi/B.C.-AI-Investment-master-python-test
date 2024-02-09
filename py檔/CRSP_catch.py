#!/usr/bin/env python
# coding: utf-8

# In[77]:


#(先將剛剛下載的Python套件import進來)
import requests
from bs4 import BeautifulSoup 


# In[78]:


#將網頁Get下來
r = requests.get("https://www.crsp.org/main-menu/crsp-action") #將此頁面的HTML GET下來
print(r.text) #印出HTML


# In[90]:


#將抓下來的資料用Beautifulsoup4轉為HTML的parser
soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
sel = soup.select("h3") #***取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel


# In[91]:


#最後寫一個迴圈將爬下來的文章標題印出來
for s in sel:
    print(s.text) 

