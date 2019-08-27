import boto3
import twitter
import os
import sys
from random import shuffle

TWEET_FILE = 'all_tweets.txt'
TWEETED_FILE = 'tweeted_tweets.txt'
LOCAL_TWEET_FILE = '/tmp/' + TWEET_FILE
LOCAL_TWEETED_FILE = '/tmp/' + TWEETED_FILE
BUCKET_NAME = 'vim-twitter-bot'

def lambda_handler(event, context):
    '''
    Tweets to the @VimTips twitter account. The handler selects a tweet at random
    from the list of available tweets in the `all_tweets` file on s3.
    '''
    ### download remote resources
    s3 = boto3.resource('s3',
            aws_access_key_id=os.environ['AWS_TOKEN'],
            aws_secret_access_key=os.environ['AWS_SECRET'])
    bucket = s3.Bucket(BUCKET_NAME)
    bucket.download_file(TWEET_FILE, LOCAL_TWEET_FILE)
    bucket.download_file(TWEETED_FILE, LOCAL_TWEETED_FILE)

    ### select the tweet
    with open(LOCAL_TWEET_FILE, 'r') as f:
        available_tweets = f.readlines()

    if len(available_tweets) == 0:
        print('no more tweets!', file=sys.stderr)
        return

    shuffle(available_tweets)
    tweet = available_tweets[0]

    remaining_available_tweets = available_tweets[1:]

    ### post the tweet
    api = twitter.Api(consumer_key = os.environ['CONSUMER_KEY'],
            consumer_secret = os.environ['CONSUMER_SECRET'],
            access_token_key = os.environ['ACCESS_TOKEN'],
            access_token_secret = os.environ['ACCESS_TOKEN_SECRET'])
    status = api.PostUpdate(tweet)

    ### update local resources
    with open(LOCAL_TWEETED_FILE, 'a+') as f:
        f.write(tweet)
    with open(LOCAL_TWEET_FILE, 'w') as f:
        for t in remaining_available_tweets:
            f.write('{}\n'.format(t))

    ### update remote resources
    bucket.upload_file(LOCAL_TWEET_FILE, TWEET_FILE)
    bucket.upload_file(LOCAL_TWEETED_FILE, TWEETED_FILE)

