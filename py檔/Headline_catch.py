#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager  #chrome時
from webdriver_manager.microsoft import EdgeChromiumDriverManager #edge時(預設瀏覽器)
from selenium.webdriver.edge.service import Service
#取得元素
#Selenium 4 不提供 find_element_by_XXX 的方法, 
#只提供取得第一個元素 find_element 或是所有元素的 find_elements 方法, 
#可以搭配 By 類別指定找尋元素的依據。
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from bs4 import BeautifulSoup
import zipfile
import time


# In[6]:


#建立Chrome Webdriver物件，並且發送請求到"證券交易所的上市公司季報"(可依照需求)網頁
domain_url = 'https://www.twse.com.tw/zh'
 
#browser = webdriver.Chrome(ChromeDriverManager().install()) #chrome時
browser = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
browser.get(
    f'{domain_url}/about/news/news/list.html')
    #後接的網址是要下載區域的子網址連結ex:https://www.twse.com.tw/zh/statistics/statisticsList?type=05&subType=225


# In[7]:


#要點擊查詢按鈕才會出現檔案資料表格
#所以就需要定位查詢按鈕元素
#可以在查詢按鈕的地方點擊滑鼠右鍵，選擇「檢查」來檢視原始碼
time.sleep(2)
select = Select(browser.find_element(By.CSS_SELECTOR, 'select#label1'))
select.select_by_value("2022")

select2 = Select(browser.find_element(By.CSS_SELECTOR, 'select#datePick1'))
select2.select_by_value("2022")

button = browser.find_element(By.CLASS_NAME,'submit')
buttons = button.find_element(By.CLASS_NAME,'search')
buttons.click()


# In[8]:


time.sleep(2)
button2 = browser.find_element(By.CLASS_NAME,'rwd-tools')
button2s = button2.find_element(By.CLASS_NAME,'csv')
button2s.click()
time.sleep(5)
browser.close()


# In[ ]:




