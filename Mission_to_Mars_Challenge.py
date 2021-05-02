#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


# In[2]:


# Set up Splinter executable Path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[9]:


# set up the html parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[10]:


slide_elem.find('div', class_='content_title')
slide_elem


# In[11]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[12]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[13]:


# Visit url
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[14]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[17]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[18]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[19]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[20]:


# import html table with pandas read_html function
df = pd.read_html('https://galaxyfacts-mars.com/')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[21]:


# pandas can convert DataFrame table back to html
df.to_html()


# In[22]:


# shutdown the automatic browser
# browser.quit()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[23]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)
time.sleep(1)


# In[35]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for hemi in range(0, 4):
    time.sleep(0.5)
    page = browser.find_by_tag('h3')
    page[hemi].click()
    
    img_html = browser.html
    hemi_soup = soup(img_html, 'html.parser')
    
    url = 'https://marshemispheres.com/'
    img_url = url + hemi_soup.find_all('a', target ='_blank')[2].get('href')
    title = browser.find_by_tag('h2').text
    hemisphere_image_urls.append({'title': title, 'img_url': img_url})
    
    browser.back()


# In[36]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[37]:


# 5. Quit the browser
browser.quit()

