#!/usr/bin/env python
# coding: utf-8

# # Web Scraping Job Vacancies

# ## Introduction
# 
# In this project, we'll build a web scraper to extract job listings from a popular job search platform. We'll extract job titles, companies, locations, job descriptions, and other relevant information.
# 
# Here are the main steps we'll follow in this project:
# 
# 1. Setup our development environment
# 2. Understand the basics of web scraping
# 3. Analyze the website structure of our job search platform
# 4. Write the Python code to extract job data from our job search platform
# 5. Save the data to a CSV file
# 6. Test our web scraper and refine our code as needed
# 
# ## Prerequisites
# 
# Before starting this project, you should have some basic knowledge of Python programming and HTML structure. In addition, you may want to use the following packages in your Python environment:
# 
# - requests
# - BeautifulSoup
# - csv
# - datetime
# 
# These packages should already be installed in Coursera's Jupyter Notebook environment, however if you'd like to install additional packages that are not included in this environment or are working off platform you can install additional packages using `!pip install packagename` within a notebook cell such as:
# 
# - `!pip install requests`
# - `!pip install BeautifulSoup`

# ## Step 1: Importing Required Libraries

# In[19]:


# your code here
get_ipython().system('pip install requests')
get_ipython().system('pip install bs4')


# In[20]:


get_ipython().system('pip install pandas')


# In[21]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[76]:


URL = "https://www.amazon.in/s?k=phones&crid=2ZZVCGTEBYHTK&sprefix=phone%2Caps%2C330&ref=nb_sb_noss_1"


# In[69]:


HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})


# In[77]:


webpage = requests.get(URL, headers=HEADERS)


# In[71]:


type(webpage.content)


# In[78]:


soup= BeautifulSoup(webpage.content, "html.parser")


# In[80]:


links= soup.find_all("a", attrs={'class': 'a-link-normal s-no-outline'})


# In[82]:


link = links[0].get('href')


# In[87]:


product_list = "https://www.amazon.in/Apple-iPhone-13-128GB-Blue/dp/B09G9BL5CP/ref=sr_1_1_sspa?crid=2ZZVCGTEBYHTK&dib=eyJ2IjoiMSJ9.RYXc3KU6MrNytq5dLjndxc1Mdm6HjbZGxBTshm5pEDzjMIM5iWmqS_QEODtI2vIESSZSZLbnH_6bnX9E666j4EWJ7Nyy_fsIP42ReSEbCnabZkqASYCAVZgbHXpPvCM4eflSrWl-fIHY4YEFP7BlsxAjlg_SlpBD5KYwhSFfJ0C7GTDHOUKV1EKNaZ478lSUROmBE9jswCgC1yq0Uf2R3hVN15i2_AtH8oLekcfJtpY.vjF8CZozfX9DBJDk52oiJfRgp5t7m6Yy9giDUWMu8ys&dib_tag=se&keywords=phones&qid=1711447619&sprefix=phone%2Caps%2C330&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"


# In[89]:


new_webpage = requests.get(product_list, headers=HEADERS)


# In[90]:


new_webpage


# In[91]:


new_soup= BeautifulSoup(new_webpage.content, "html.parser")


# In[117]:


title = new_soup.find("span", attrs={"id": 'productTitle'})


# In[119]:


price = soup.find("span", attrs={'id':'priceblock_ourprice'}) 


# In[121]:


rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'})


# In[123]:


review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}) 


# In[126]:


available = soup.find("div", attrs={'id':'availability'})


# In[128]:


d = {"title":[], "price":[], "rating":[], "reviews":[],"availability":[]}


# In[129]:


amazon_df = pd.DataFrame.from_dict(d)


# In[130]:


amazon_df


# In[81]:


links


# In[131]:


link


# In[93]:


new_soup


# In[88]:


product_list


# In[79]:


soup

