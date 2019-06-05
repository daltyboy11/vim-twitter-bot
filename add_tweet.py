import sqlite3
import argparse
from typing import Tuple

MAX_TWEET_LENGTH=280
CATEGORIES=["fact", "tip"]
SUBCATEGORIES=["navigation", "substitution", "ex", "command-line", "search", "none"]
INSERT_STATEMENT='insert into tweets (category, subcategory, tweet) values (\'{}\', \'{}\', \'{}\');'

def parse_args() -> Tuple[str, str, str]:
    parser = argparse.ArgumentParser(description='Parse tweet information')
    parser.add_argument("--category", type=str)
    parser.add_argument("--subcategory", type=str)
    parser.add_argument("--tweet", type=str)
    args = parser.parse_args()

    assert args.category in CATEGORIES, "category must be one of {}".format(CATEGORIES)
    assert args.subcategory in SUBCATEGORIES, "subcategory must be one of {}".format(SUBCATEGORIES)
    assert len(args.tweet) <= MAX_TWEET_LENGTH, "tweet cannot exceed {} characters".format(args.tweet)

    return (args.category, args.subcategory, args.tweet)

if __name__ == '__main__':
    category, subcategory, tweet = parse_args();

    conn = sqlite3.connect('tweets.db')
    c = conn.cursor()
    insert_statement=INSERT_STATEMENT.format(category, subcategory, tweet)
    print(insert_statement)
    c.execute(INSERT_STATEMENT.format(category, subcategory, tweet))
    conn.commit()
    conn.close()
