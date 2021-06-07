#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver


# In[2]:


from bs4 import BeautifulSoup as Soup


# In[3]:


from selenium.webdriver.common.by import By


# In[4]:


from selenium.webdriver.common.keys import Keys


# In[5]:


from selenium.webdriver.common.action_chains import ActionChains


# In[6]:


import time


# In[7]:


import json


# In[ ]:





# In[8]:


driver=webdriver.Chrome()


# In[9]:


driver.get("https://tw.news.yahoo.com/entertainment")


# In[ ]:





# In[10]:


driver=webdriver.Chrome()#開啟driver搜尋頁面
driver.get("https://tw.news.yahoo.com/entertainment")
news_list=[]  #定義一個news的存放list後續資料都儲存於此


# In[11]:


n_scroll=40
for i in range(n_scroll):
    driver.find_element_by_xpath('//*[@id="Col1-1-Hero-Proxy"]/div/ul/li/div/a').send_keys(Keys.PAGE_DOWN)
    #利用for迴圈的方式抓取xpath為//*[@id="Col1-1-Hero-Proxy"]/div/ul/li/div/a的網頁元素


# In[12]:


def load_page(xpath): #載入頁面
    try:
        link=driver.find_element_by_xpath(xpath)#透過xpath的方式取得文章路徑
        ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform() #開啟新分頁
        driver.switch_to.window(driver.window_handles[-1]) #跳至新開頁面
        news_data=get_content()#使用Get Content方法取得需要的資料與資料屬性
        news_list.append(news_data) #抓取內容並儲存到news_list
        driver.close() #關閉新分頁
        driver.switch_to.window(driver.window_handles[-1]) #跳回原頁面
    except:
        pass
        #跳過不符合文章配置的廣告內容


# In[13]:


def get_content():
    html=driver.page_source
    soup=Soup(html,'lxml')
    for article in soup.select('.caas-container'):
        title=article.select('.caas-title-wrapper')[0].text
        url=driver.current_url
        try:
            yimg=soup.select('figure div div div img')[0].get('src')
        except:
            yimg=""
        content=soup.select('div div div div div div div p')[0].text
        news_data={'title': title, 'url': url, 'yimg': yimg, 'content': content}
    return news_data


# In[14]:


#因為上下文章頁面格式比不同因此上面特別做設定處理
xpath='//*[@id="Col1-1-Hero-Proxy"]/div/ul/li/div/a' #用檢查得到的文章資料屬性格式定義Xpath變數
load_page(xpath) #再利用loadpage的方法把變數輸入去進入頁面進行資料取得的下一步驟
xpath='//*[@id="Col1-2-CategoryWrapper-Proxy"]/div/div[1]/ul[1]/li/div/a'
load_page(xpath)
xpath='//*[@id="Col1-2-CategoryWrapper-Proxy"]/div/div[2]/ul[1]/li/div/a'
load_page(xpath)
xpath='//*[@id="Col1-3-CategoryWrapper-Proxy"]/div/div[1]/ul[1]/li/div/a'
load_page(xpath)
xpath='//*[@id="Col1-3-CategoryWrapper-Proxy"]/div/div[2]/ul[1]/li/div/a'
load_page(xpath)

#後續文章格式就相同所以用迴圈就好
for i in range(15):
    xpath = '//*[@id="YDC-Stream"]/ul/li['+ str(i+1) +']/div/div/div[2]/h3/a'
    load_page(xpath)


# In[65]:


with open('yahoo-news.json', 'w', encoding='utf-8') as f:
    json.dump(news_list, f)


# In[66]:


with open('yahoo-news.json', 'r', encoding='utf-8') as f:
    output=json.load(f)
print(output)


# In[ ]:





# In[ ]:




