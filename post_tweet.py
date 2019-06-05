import sqlite3
from typing import Tuple
import twitter
import os

CONSUMER_KEY=os.environ['VIM_TIPS_AND_TRICKS_CONSUMER_KEY']
CONSUMER_SECRET=os.environ['VIM_TIPS_AND_TRICKS_CONSUMER_SECRET']
ACCESS_TOKEN_KEY=os.environ['VIM_TIPS_AND_TRICKS_ACCESS_TOKEN_KEY']
ACCESS_TOKEN_SECRET=os.environ['VIM_TIPS_AND_TRICKS_ACCESS_TOKEN_SECRET']
TWEETS_DB=os.environ['TWEETS_DB']

def get_tweet() -> Tuple[int, str]:
    conn = sqlite3.connect(TWEETS_DB)
    c = conn.cursor()
    c.execute('select (id, tweet) from tweets where tweet_date is null;')
    c.commit();
    result = c.fetchone()
    conn.close()
    return (int(result[0]), str(result[1]))

def record_tweet(tweet_id: int):
    conn = sqlite3.connect(TWEET_DB)
    c = conn.cursor()
    # TODO

if __name__ == '__main__':
    api = twitter.Api(consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            access_token_key=ACCESS_TOKEN_KEY,
            access_token_secret=ACCESS_TOKEN_SECRET)

    tweet_id, tweet_text = get_tweet()
    
    try:
        api.PostUpdate(tweet_text)
        # TODO


