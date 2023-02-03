import pandas as pd
import re
import emoji
# this will skip tweets that have mentions or links
clean_tweets = []  # where we will push filtered tweets in

unclean_tweets = pd.read_csv('your-unclean-tweets.csv')  # fetch unclean possibly duplicate tweets

URL_REGEX = r"""((?:(?:https|ftp|http)?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|org|uk)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|uk|ac)\b/?(?!@)))"""

MENTION_REGEX = "@[A-Za-z0-9]+"
for tweet in unclean_tweets['Tweet']:

    mentions = re.findall(MENTION_REGEX, str(tweet))
    if len(mentions) > 0:
        continue # skip tweets that have one or more mentions
    urls = re.findall(URL_REGEX, str(tweet))
    if len(urls) > 0:
        continue  # skip tweets that have one or more links
    tweet = ''.join(c for c in str(tweet) if c not in emoji.EMOJI_DATA)  # Remove Emojis but keep text
    tweet = tweet.replace("#", "").replace("_", " ")  # Remove hashtag sign but keep the text
    clean_tweets.append(tweet)

df = pd.DataFrame(clean_tweets, columns=['Tweet'])
df.drop_duplicates()  # remove all duplicates
df.to_csv("to-clean-tweets.csv")
