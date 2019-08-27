import sys
import boto3
import os

ALL_TWEETS_FILE = 'all_tweets_safe.txt'
TWEET_FILE = 'all_tweets.txt'
LOCAL_TWEET_FILE = '/tmp/' + TWEET_FILE
BUCKET_NAME = 'vim-twitter-bot'
MAX_TWEET_LEN = 280

def upload(tweet):
    '''
    Uploads the tweet to s3 and also writes tweet to local copy of all tweets
    '''
    if len(tweet) > MAX_TWEET_LEN:
        print('tweet too long', file=sys.stderr)

    s3 = boto3.resource('s3',
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])
    bucket = s3.Bucket(BUCKET_NAME)
    bucket.download_file(TWEET_FILE, LOCAL_TWEET_FILE)
    
    ### write to tweeted file
    with open(LOCAL_TWEET_FILE, 'a+') as f:
        f.write(tweet)

    ### write to all tweets file for reference
    with open(ALL_TWEETS_FILE, 'a+') as f:
        f.write(tweet)

    bucket.upload_file(LOCAL_TWEET_FILE, TWEET_FILE)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python3 upload_tweet.py tweet', file=sys.stderr)

    upload(sys.argv[1])
