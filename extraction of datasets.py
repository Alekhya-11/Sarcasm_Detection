import os
import tweepy as tw
import pandas as pd


consumer_key= 'your consumer key'
consumer_secret= 'your consumer secret key'
access_token= 'your access token'
access_token_secret= 'your access token secret'


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "sarcasm"
date_since = "2020-11-16"


tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)
tweets



tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)

# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)
    
    
    
    tweets = tw.Cursor(api.search,
                       q=search_words,
                       lang="en",
                       since=date_since).items(5)

# Collect a list of tweets
[tweet.text for tweet in tweets]



tweets = tw.Cursor(api.search,
                       q=search_words,
                       lang="en",
                       since=date_since).items(50)

# Collect a list of tweets
[tweet.text for tweet in tweets]



new_search = search_words + " -filter:retweets"
new_search



tweets = tw.Cursor(api.search,
                       q=new_search,
                       lang="en",
                       since=date_since).items(5)

[tweet.text for tweet in tweets]
