import credentials
import tweepy 
import pandas as pd
import re

auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit= True)
#new_search = "hugo+app -filter:retweets"

new_search = "pokemon"
max_tweets = 1000

tweets = tweepy.Cursor(api.search,
                   q=new_search,
                   lang="en",
                   tweet_mode='extended',
                   since='2021-09-01').items(max_tweets)
 
# Pulling information from tweets iterable object
# Add or remove tweet information you want in the below list comprehension
tweets_list = [[tweet.full_text, tweet.created_at, tweet.id_str, tweet.user.screen_name, tweet.user.location,
                tweet.retweet_count, tweet.favorite_count, tweet.lang, tweet.source] for tweet in tweets]
 
# Creation of dataframe from tweets_list
# Add or remove columns as you remove tweet information
tweets_df = pd.DataFrame(tweets_list,columns=['Tweet Text', 'Tweet Datetime', 'Tweet Id', 'Twitter @ Name', 'Place Info',
                                              'Retweets', 'Favorites', 'Language', 'Source'])


#Cleaning the text
def cleanTxt(text):
    text = re.sub(r'@[A-Za-z0-9]+','',text) #Remove @mentions
    text = re.sub(r'#','',text) #Removing the # symbol
    text = re.sub(r'RT[\s]+','',text) #Removing RT
    text = re.sub(r'https?:\/\/\S+','',text) #Removecthe hyperlink

    return text

#Cleaning text
tweets_df['Tweet Text_cln'] = tweets_df['Tweet Text'].apply(cleanTxt)

#sentiment analysis using TextBlob
from textblob import TextBlob as blob

#Create function to get subjetivity
def getSubjectivity(text):
    return blob(text).sentiment.subjectivity

def getPolarity(text):
    return blob(text).sentiment.polarity

#Create 2 new columns, subjetivity, polarity
tweets_df['Subjectivity'] = tweets_df['Tweet Text_cln'].apply(getSubjectivity)
tweets_df['Polarity'] = tweets_df['Tweet Text_cln'].apply(getPolarity)

#Show new df
print(tweets_df)
#Creation of csv file to store and export tweets
tweets_df.to_csv("tweets_pokemon2.csv",encoding='utf-8-sig')
