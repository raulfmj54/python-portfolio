import credentials
import tweepy 
import pandas as pd
import sys
import got


auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


tweetCriteria = got.manager.TweetCriteria().setQuerySearch('hugo_app').setSince("2021-08-01").setUntil("2021-08-30").setMaxTweets(850)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)

print("### Example 2 - Get tweets by query search [hugo app]", tweet)


import got

tweetCriteria = got.manager.TweetCriteria().setQuerySearch('europe refugees').setSince("2015-05-01").setUntil("2015-09-30").setMaxTweets(1)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
	  
print(tweet.text) 