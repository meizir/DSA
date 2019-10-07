#!/usr/bin/env python
# coding: utf-8

# In[7]:


# settings
from IPython.display import display, Markdown

# import lib
import numpy as np
import pandas as pd

# data is store in github 
google_play_apps = pd.read_csv("https://github.com/meizir/DSA/blob/master/Basic%20Python%20Programming/googleplaystore.zip?raw=true", 
                                     compression='zip')

display(Markdown("<br>Sample data used in this analysis : <br>"))
google_play_apps.head()


# In[8]:


# retrieve dataframe
dataset_shape = google_play_apps.shape

# print result row & collums
display(Markdown("In the dataset of googleplaystore.csv, it consists of `%d` rows and `%d` columns" % dataset_shape));


# In[12]:


# get unique apps category 
unique_category = google_play_apps["Category"].unique()
unique_category_number = google_play_apps["Category"].nunique()

# print result apps category 
display(Markdown("In the dataset of googleplaystore.csv, it consists of `%d` unique apps categories." % unique_category_number));


# In[11]:


# get unique genres 
unique_genre_original = google_play_apps["Genres"].unique()
unique_genre_original_number = google_play_apps["Genres"].nunique()

# split unige genre by ';'
unique_genre_splitted = np.unique(';'.join(unique_genre_original).split(";"))
unique_genre_splitted_number = len(unique_genre_splitted)

# print result
display(Markdown("In the dataset of googleplaystore.csv, as is, it consists of `%d` unique apps genres string." % unique_genre_original_number));
#display(Markdown("Which are `" + "`, `".join(unique_genre_original) + "`"));


# In[13]:


google_play_apps.drop_duplicates(subset='App', inplace=True)


# In[14]:


google_play_apps[google_play_apps['Installs']=='Free']


# In[15]:


google_play_apps = google_play_apps[google_play_apps['Installs'] != 'Free']


# In[16]:


google_play_apps['Installs'] = google_play_apps['Installs'].apply(lambda x: x.replace('+', '') if '+' in str(x) else x)


# In[18]:


google_play_apps['Installs'] = google_play_apps['Installs'].astype(int)


# In[19]:


# make match Apps and Category
apps_to_be_matched = ["Subway Surfers", "Dropbox", "File Commander - File Manager/Explorer", "WhatsApp Messenger", "Flipboard: News For Our Time", 
                      "Pinterest", "FIFA Soccer", "DU Battery Saver - Battery Charger & Battery Life"]

# filter google_play_apps using row where Apps in app_to_be_matched and select only App and Category columns only

apps_category_df = google_play_apps.loc[google_play_apps['App'].isin(apps_to_be_matched), ['App', 'Category']]


# sort according to Q7 (app_to_be_mathced)
apps_category_df['App'] = apps_category_df['App'].astype("category")
apps_category_df['App'].cat.set_categories(apps_to_be_matched, inplace=True)

apps_category_df.sort_values(['App']).reset_index(drop=True)


# In[20]:


# is app 1 billion users
apps_is_1bio = ["Skype", "Google Duo - High Quality Video Calls", "Facebook", "WhatsApp Messenger"]

# filter google_play_apps using row where Apps in apps_is_1bio and select only App and Installs columns only
# Note we use contains  because there are different version of 'Skype'
apps_is_1bio_df = google_play_apps.loc[google_play_apps['App'].str.contains('Skype') | google_play_apps['App'].isin(apps_is_1bio),
                                       ['App', 'Installs']]

apps_is_1bio_df["App_edit"] = np.where(apps_is_1bio_df['App'].str.contains('Skype'), 'Skype', apps_is_1bio_df['App'])

# is 1 bio columns
apps_is_1bio_df['is_1bio'] = apps_is_1bio_df['Installs'] >= 1000000000

# sort according to Q7 (app_to_be_mathced)
apps_is_1bio_df['App_edit'] = apps_is_1bio_df['App_edit'].astype("category")
apps_is_1bio_df['App_edit'].cat.set_categories(apps_is_1bio, inplace=True)
apps_is_1bio_df.sort_values(['App_edit']).reset_index(drop=True)


# In[21]:


# filter `COMMUNICATION` categoty apps and select `App`, `Category` and `Reviews`
communication_apps_df = google_play_apps.loc[google_play_apps['Category'] == "COMMUNICATION", ['Category', 'App', 'Reviews']]

# cast string to integer
communication_apps_df['Reviews'] = communication_apps_df['Reviews'].astype(int)

# sort descending
communication_apps_df.sort_values(['Reviews'], ascending=False).reset_index(drop=True).head(10)


# In[22]:


# filter `GAME` categoty apps and select `App`, `Category`, `Installs` and `Rating`
game_apps_df = google_play_apps.loc[google_play_apps['Category'] == "GAME", 
                                             ['Category', 'App', 'Installs', "Rating"]]

# sort descending
game_apps_df.sort_values(['Installs', 'Rating'], ascending=False).reset_index(drop=True).head(3)


# In[ ]:




