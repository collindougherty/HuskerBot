# NOTICE #

# THIS FILE IS LIVE #
# DONT RUN THIS FILE #

import functions as f
api = f.api

# count represents the number of tweets to be retweeted per user in retweets.py
try:
    f.retweet_bunch(api, count = 1)
    print("success")
except:
    print("error")