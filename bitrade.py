import tweepy
import time
import pandas as pd


consumer_key = "KnEgWcuf6TZbg3EudjGhEbUv1"
consumer_secret = "z8V3LbFNw99sMqgw5GS5V2c4Z6reIcZedBGuqvfZTrU2GMGwkx"
access_token = "1110384185594662912-vWqz5akgBvJqmvisVP4TtD6YhVnC78"
access_token_secret = "ZR7DRcaedIjPvwMIug92W5vxGiIijaFeozd5CsKamQ3nE"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

username = 'elonmusk'
count = 3
try:     
 # Creation of query method using parameters
 tweets = tweepy.Cursor(api.user_timeline,id=username).items(count)
 
 # Pulling information from tweets iterable object
 tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
 
 # Creation of dataframe from tweets list
 # Add or remove columns as you remove tweet information
 tweets_df = pd.DataFrame(tweets_list)
except BaseException as e:
      print('failed on_status,',str(e))
      time.sleep(0)

#print(tweets_df)

#print rows function
#for index, row in tweets_df.iterrows():
 #   print(row[int(2)], row[int(2)])


trigger_words = ["Much wow!", "doge", "moon", "currency"]

for index, row in tweets_df.iterrows():
    if any(map((row[int(2)], row[int(2)]).__contains__, trigger_words)):
        print("ELON TWEETED ABOUT DOGE")


        
