# hacker-news-predictions
predict what news articles on Hacker News (news.ycombinator.com) I will read based on browser history

## Items in my browser history:

    $ cp ~/Library/Application\ Support/Google/Chrome/Default/History 
    $ sqlite3 History "select datetime(last_visit_time/1000000-11644473600,'unixepoch'),url from  urls order by last_visit_time asc" | wc -l
       20243
    $ sqlite3 History "select url from urls" |\
         grep //news\.ycombinator | grep "item?id=" |\
         sed 's/https:\/\/news\.ycombinator\.com\/item?id=//' | sed 's/#.*//' |\
         sort | uniq > hnews_IDs_I_visited.log

from https://bgstack15.wordpress.com/2019/04/07/read-chrome-history-from-command-line/

Python version: see https://github.com/umbcdata601/spring2020/blob/master/jupyter_notebooks/week_07_math/histogram%20of%20my%20Chrome%20history.ipynb
