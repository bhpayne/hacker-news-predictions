#!/usr/bin/env python3
import requests
import re
import pickle

from urllib.parse import urlparse
# pip install nltk
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt') # word tokenization
nltk.download('stopwords')
en_stops = set(stopwords.words('english'))

"""
build a table of items versus features
"""

base_url = 'https://hacker-news.firebaseio.com/v0/'

# API documentation: https://github.com/HackerNews/API
# endpoints:
#    item/<ID>.json
#    user/<ID>.json
#    topstories.json
#    askstories.json
#    showstories.json
#    jobstories.json
#    updates.json

def remove_stopwords(list_of_words: list) -> list:
    """
    
    >>> remove_stopwords(["a","great","title"])
    ['great', 'title']
    """
    new_list = []
    for word in list_of_words:
        if word not in en_stops:
            new_list.append(word)
    return new_list

def list_of_words_in_title(title: str) -> list:
    """
    from https://github.com/umbcdata601/spring2020/blob/master/jupyter_notebooks/week_09_clustering/nltk_for_text_processing.ipynb
    
    >>> list_of_words_in_title("a great title")
    ['great', 'title']
    """
    word_tokens = word_tokenize(title)
    word_tokens = [word.lower() for word in word_tokens]
    word_tokens_no_stopwords = remove_stopwords(word_tokens)
    return word_tokens_no_stopwords

def get_domain_from_url(url: str) -> str:
    """
    
    >>> get_domain_from_url("http://www.google.com/a/folder/for/content")
    "google.com"
    """
    # https://stackoverflow.com/questions/44113335/extract-domain-from-url-in-python
    domain = urlparse(url).netloc
    if domain.startswith('www.'):
        domain = domain.replace('www.','')
    return domain.lower()

def list_of_words_in_url(url: str) -> list:
    """
    
    >>> list_of_words_in_url("http://www.google.com/a/folder/for/content")
    ['folder','content']
    """
    # https://stackoverflow.com/questions/44113335/extract-domain-from-url-in-python
    path = urlparse(url).path
    # https://stackoverflow.com/a/1059596/1164295
    words_as_list = re.findall(r"[\w']+", path)
    words_as_list = [word.lower() for word in words_as_list]
    words_as_list_no_stopwords = remove_stopwords(words_as_list)
    return words_as_list_no_stopwords
    
with open('hnews_IDs_I_visited.log', 'r') as fil:
    list_of_IDs = fil.read().split('\n')

item_feature_table = []
list_of_items = []
for item_id in list_of_IDs:
    feature_dict = {}
    feature_dict['id']=item_id
    endpoint = base_url + 'item/'+str(item_id)+'.json'
    item = requests.get(endpoint)
    # {"by":"anigbrowl",
    #  "descendants":215,                      # In the case of stories or polls, the total comment count
    #  "id":24438027,
    #  "kids":[2444015,24439038,24439670],     # top-level comment IDs
    #  "score":156,
    #  "time":1599784095,
    #  "title":"Vinyl LPs Sell More Than CDs for the First Time in 3 Decades",
    #  "type":"story",
    #  "url":"http://www.syntia.com/content/2020/09/10/vinyl-lps-sell-more-than-/"}
    list_of_items.append(item.json())
    if item.json()['type']=='story':
        if 'by' in item.json().keys():
            feature_dict['by']=item.json()['by']
        else:
            feature_dict['by']=""
        if "score" in item.json().keys():
            feature_dict["score"]=item.json()["score"]
        else:
            feature_dict["score"]=0
        if "title" in item.json().keys():
            #feature_dict["title"]=item.json()["title"]
            feature_dict["title words"] = list_of_words_in_title(item.json()["title"])
        else:
            feature_dict["title"]=""
        if "url" in item.json().keys():
            #feature_dict["url"]=item.json()["url"]
            feature_dict["url domain"]=get_domain_from_url(item.json()["url"])
            feature_dict["url words"]=list_of_words_in_url(item.json()["url"])
        else:
            feature_dict["url"]=""
        if "descendants" in item.json().keys():
            feature_dict["descendants"]=item.json()["descendants"]
        else:
            feature_dict["descendants"]=0
        
        item_feature_table.append(feature_dict)

        # https://wiki.python.org/moin/UsingPickle
        pickle.dump( item_feature_table, open( "item_features_list_of_dicts.pkl", "wb" ) )