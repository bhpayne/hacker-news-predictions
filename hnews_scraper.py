#!/usr/bin/env python3
import requests

"""
My favorite alternative interface: http://hnrankings.info/6/1-10/
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

try:
    top_stories = requests.get(base_url + 'topstories.json')
except Error as err:
    print(str(err))
    exit()

list_of_stories = []
for item_id in top_stories.json():
    story = requests.get(base_url + 'item/'+str(item_id)+'.json')
    # {"by":"anigbrowl",
    #  "descendants":215,                                                             # In the case of stories or polls, the total comment count
    #  "id":24438027,
    #  "kids":[2444015,24439038,24439670,24439797,24440976,24439996],                 # top-level comment IDs
    #  "score":156,
    #  "time":1599784095,
    #  "title":"Vinyl LPs Sell More Than CDs for the First Time in 3 Decades",
    #  "type":"story",
    #  "url":"http://www.syntia.com/content/2020/09/10/vinyl-lps-sell-more-than-/"}
    list_of_stories.append(story.json())
