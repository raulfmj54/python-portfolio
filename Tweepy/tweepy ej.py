import credentials
import tweepy 
import pandas as pd

auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


#new_search = "hugo+app -filter:retweets"
new_search = "hugo+app -filter:retweets"

tweets = tweepy.Cursor(api.search,
                   q=new_search,
                   lang="es",
                   since='2020-01-01').items(1000)



all_tweets = [tweet.text for tweet in tweets]
all_tweets_df = pd.DataFrame(data=all_tweets,
                    columns=['Tweet'])
print(all_tweets[:5])
print(all_tweets_df)

print()
print("Twitter user data:")
tweets = tweepy.Cursor(api.search, 
                           q=new_search,
                           lang="es",
                           since='2018-01-01').items(1000)

users_locs = [[ tweet.user.screen_name,tweet.user.location] for tweet in tweets]

tweet_text = pd.DataFrame(data=users_locs, 
                    columns=['user', "location"])



all_tweets_df[["user", "location"]] = tweet_text
print(all_tweets_df)
