#!/usr/bin/env python
# coding: utf-8

# In[1]:


def billboard():
    # import libraries
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup
    from tqdm.notebook import tqdm
    # get the website url
    url = 'https://www.billboard.com/charts/hot-100'
    # run request on url
    response = requests.get(url, headers = {"Accept-Language" : "en-US"})
    # make the soup
    soup = BeautifulSoup(response.content,'html.parser')
    
    # assemble all the information creating lists
    rank_position=[]
    song_title=[]
    song_author=[]

    len_song=len(soup.select('h3.c-title.a-no-trucate'))
    len_song_check=len(soup.select('span.c-label.a-no-trucate.a-font-primary-s'))
    # loop over the songs and authors
    for i in tqdm(range(len_song)):
        rank_position.append(i+1)
        song_title.append(soup.select('h3.c-title.a-no-trucate')[i].get_text(strip = True))
        song_author.append(soup.select('span.c-label.a-no-trucate.a-font-primary-s')[i].get_text(strip = True))
    # create a clean df of this information
    df = pd.DataFrame({'position': rank_position,
                             'song':song_title,
                             'author':song_author})
    df = df.applymap(lambda s:s.lower() if type(s) == str else s)
    return (df)


# In[ ]:




