import pandas as pd
import re
import emoji

clean_tweets = []
unclean_tweets = pd.read_csv('your-half-clean-tweets.csv')
for tweet in unclean_tweets['Tweets']:
    tweet = re.sub("@[A-Za-z0-9]+","",str(tweet)) #Remove first apperance @ sign
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", str(tweet)) #Remove http links --first apperance
    tweet = " ".join(tweet.split())
    tweet = ''.join(c for c in str(tweet) if c not in emoji.EMOJI_DATA) #Remove Emojis
    tweet = str(tweet).replace("#", "").replace("_", " ") #Remove hashtag sign but keep the text
    clean_tweets.append(tweet)
df = pd.DataFrame(clean_tweets, columns=['Tweet'])
df.drop_duplicates()
df.to_csv("to-your-full_clean_tweets.csv")

