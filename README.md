# hacker-news-predictions
predict what news articles on Hacker News (news.ycombinator.com) I will read based on browser history

## 1. HackerNews Items in my browser history:

    $ cp ~/Library/Application\ Support/Google/Chrome/Default/History 
    $ sqlite3 History "select datetime(last_visit_time/1000000-11644473600,'unixepoch'),url from  urls order by last_visit_time asc" | wc -l
       20243
    $ sqlite3 History "select url from urls" |\
         grep //news\.ycombinator | grep "item?id=" |\
         sed 's/https:\/\/news\.ycombinator\.com\/item?id=//' | sed 's/#.*//' |\
         sort | uniq > hnews_IDs_I_visited.log

from https://bgstack15.wordpress.com/2019/04/07/read-chrome-history-from-command-line/

Python version: see https://github.com/umbcdata601/spring2020/blob/master/jupyter_notebooks/week_07_math/histogram%20of%20my%20Chrome%20history.ipynb

## 2. get features associated with HN Items I've browsed

    python get_stories_I_visited.py
    
## 3. get features associated with HN Items I did not access

## 4. train a recommender

use Content-Based Filtering; see https://www.kaggle.com/gspmoreira/recommender-systems-in-python-101

There are multiple options; pros/cons not known to me currently
 * create TF-IDF array first from features, then use cosine similarity to make prediction 
   * https://www.kaggle.com/gspmoreira/recommender-systems-in-python-101
   * https://heartbeat.fritz.ai/recommender-systems-with-python-part-i-content-based-filtering-5df4940bd831
   * https://medium.com/analytics-vidhya/content-based-recommender-systems-in-python-2b330e01eb80
   * https://medium.com/@bindhubalu/content-based-recommender-system-4db1b3de03e7
 * https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html ?

## 5. pull current news stories

    python get_top_stories.py

## 6. use the recommender against new stories to produce suggestions


## 7. post to 
