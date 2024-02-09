#!/usr/bin/env python
# coding: utf-8

# In[1]:


#請先記得裝 pip install torch transformers
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

import csv


# In[2]:


# 開啟 CSV 檔案
with open('newsList.csv', newline='') as csvfile:

    # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
    rows = csv.DictReader(csvfile)

    # 以迴圈輸出指定欄位
    for row in rows:
        #print(row['標題'],row['連結'],row['日期'])
        print(row['標題'])


# In[3]:


# 加載預訓練的GPT-2模型和分詞器
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)


# In[17]:


# 定義一個函數來進行問題回答
#def generate_response(prompt, max_length=200):
    #input_ids = tokenizer.encode(prompt, return_tensors="pt")
    #output = model.generate(input_ids, max_length=max_length, num_return_sequences=1)
    #response = tokenizer.decode(output[0], skip_special_tokens=True)
    #return response

# 设置填充标记
model.config.pad_token_id = model.config.eos_token_id

def generate_response(prompt, max_length=500):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)  # 设置注意力掩码
    output = model.generate(input_ids, attention_mask=attention_mask, max_length=max_length, num_return_sequences=1)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response


# In[18]:


#測試一個問題
question="請依此新聞標題:「112年第1季得為上市認購（售）權證（含牛熊證）之標的證券」判斷此新聞的走向"
response = generate_response(question)
print("回答:", response)


# In[5]:


#測試全部資料標題的個問題
# 發送問題並獲取答案
# 開啟 CSV 檔案
with open('newsList.csv', newline='') as csvfile:

    # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
    rows = csv.DictReader(csvfile)

    # 以迴圈輸出指定欄位
    for row in rows:
        question=(f"請依此新聞標題:「{row['標題']}」判斷此新聞的走向")
        response = generate_response(question)
        print("回答:", response)

