from config import db
from plot import updateIndexPlots
from twitter import getTwitterSentiment
from news import getNewsSentiment
from datetime import datetime
import json
import sqlite3

# inserts data for this index into database
def insertData(index):

    date = datetime.date(datetime.now())

    if index == 'DOW30':
        data = getIndexData('DOW30.json')
        for stock in data:
            db.execute("INSERT INTO DOW30 VALUES (?,?,?,?,?,?)",
            (stock['ticker'], stock['twitter_sentiment'], stock['news_sentiment'],
            stock['num_tweets'], stock['num_news'], date))
    else:
        data = getIndexData('NASDAQ100.json')
        for stock in data:
            db.execute("INSERT INTO NASDAQ100 VALUES (?,?,?,?,?,?)",
            (stock['ticker'], stock['twitter_sentiment'], stock['news_sentiment'],
            stock['num_tweets'], stock['num_news'], date))

    return

def getIndexData(json_file):

    # load in the list of DOW 30 stocks into a array of JSON dicts
    dict = {}
    with open('data/' + json_file, 'r') as infile:
        index = json.load(infile)['stocks']

    # list of stocks and thier sentiment values
    sentiments = []

    # analyze the news articles
    for stock in index:
        ticker = stock['ticker']
        full_name = stock['full_name']

        results = getNewsSentiment(ticker, full_name)
        twitter_results = getTwitterSentiment(ticker, full_name)

        # add the num and sentiment elements into results
        results['twitter_sentiment'] = twitter_results['twitter_sentiment']
        results['num_tweets'] = twitter_results['num_tweets']

        sentiments.append(results)

    return sentiments

# when the file is called, will update both tables and plots
if __name__ == "__main__":
    #insertData('DOW30')
    #insertData('NASDAQ100')
    updateIndexPlots('DOW30')
    updateIndexPlots('NASDAQ100')
