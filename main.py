import snscrape.modules.twitter as sntwitter
import pandas as pd



query = "(الحج until:2022-12-10 since:2008-01-01)"
query2 = "(until:2022-12-10 since:20010-01-01 يوم عرفة)"
query3 = "(until:2022-12-10 since:20010-01-01 المشاعر المقدسة)"
query4 = "(until:2022-12-10 since:20010-01-01 العمرة)"
query5 = "(until:2022-12-10 since:20010-01-01 الجمرات)"
query6 = "(until:2022-12-10 since:20010-01-01 مسجد نمرة)"
query7 = "(until:2022-12-10 since:20010-01-01 جبل الرحمة)"
query8 = "(until:2022-12-10 since:20010-01-01 عرفات)"
query9 = "(until:2022-12-10 since:20010-01-01 عرفة)"
query10 = "(until:2022-12-10 since:20010-01-01 مزدلفة)"
query11 = "(until:2022-12-10 since:20010-01-01 منى)"


tweets = []
limit = 50000
limit1 = 25000
limit2 = 30000
limit4 = 20000
counter = 0

for tweet in sntwitter.TwitterSearchScraper(query, query2).get_items():

    if counter == limit:
        counter = 0
        break
    else:
        tweets.append([tweet.content])
        counter = counter + 1

for tweet in sntwitter.TwitterSearchScraper(query3, query9).get_items():

    if counter == limit2:
        counter = 0
        break
    else:
        tweets.append([tweet.content])
        counter = counter + 1


for tweet in sntwitter.TwitterSearchScraper(query4, query5).get_items():

    if counter == limit1:
        counter = 0
        break
    else:
        tweets.append([tweet.content])
        counter = counter + 1

for tweet in sntwitter.TwitterSearchScraper(query7, query8).get_items():

    if counter == limit4:
        counter = 0
        break
    else:
        tweets.append([tweet.content])
        counter = counter + 1

for tweet in sntwitter.TwitterSearchScraper(query10, query11).get_items():

    if counter == limit1:
        counter = 0
        break
    else:
        tweets.append([tweet.content])
        counter = counter + 1

df = pd.DataFrame(tweets, columns=['Tweet'])
df.to_excel("Tweets.xlsx")

print(tweets.__len__())
