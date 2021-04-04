import tweepy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2


from nltk.sentiment.vader import SentimentIntensityAnalyzer


def getCovidSentiment():

    plt.style.use('fivethirtyeight')


    consumer_key = "q9ZAAGzvkOwhBwCCwj95EjV6p"
    consumer_secret = "45hffFWt9cPEHN3QWEPOzh4Kc3KKm3lazYMgRXPFYVRlPr1Bmt"
    access_token = "1378411001218002950-Lpz0TWyrx0vt5s3hx3CdgJAkYayCDH"
    access_token_secret = "692hLljgmLOEJwNV3fCQ1xrYzoWxg7cd3gmB3XMXnmb3L"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    user = api.me()

    tweets = []

    for page in range(1, 5):
        tweets.extend(api.user_timeline(screen_name="V2019N", count=200, page=page))

    own_tweets = [tweet for tweet in tweets if tweet.retweeted == False and "RT @" not in tweet.text]

    df = pd.DataFrame(data=[[tweet.created_at, tweet.text, len(tweet.text), tweet.id, tweet.favorite_count, tweet.retweet_count] for tweet in own_tweets], columns=['Date', 'Tweet', 'Length', 'ID', 'Likes', 'Retweets'])


    vader = SentimentIntensityAnalyzer()
    f = lambda tweet: vader.polarity_scores(tweet)['compound']
    df['Sentiment'] = df['Tweet'].apply(f)
    df['Date'] = pd.to_datetime(df['Date']).dt.date
    df['Sentiment'].plot(kind='hist', bins=20, figsize=(5,8), ec='black')
    plt.xlabel('Sentiment')
    plt.ylabel('Frequency')
    plt.title('Sentiment of Tweets by Covid-19')
    plt.show()


    date_df = df.groupby(['Date']).mean().reset_index()

    date_df.plot(kind='line', x='Date', y='Sentiment', figsize=(13,8), ylim=[-1,1])
    plt1.axhline(y=0, color='black')
    plt1.ylabel('Average Sentiment')
    plt1.title('Daily Average Sentiment of Tweets')
    plt1.show()

    from wordcloud import WordCloud, STOPWORDS

    text = " ".join(text for text in df.Tweet)

    stopwords = set(STOPWORDS)
    stopwords.update(["HTTPS", "CO"])

    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

    plt2.imshow(wordcloud, interpolation='bilinear')
    plt2.axis('off')
    plt2.show()

