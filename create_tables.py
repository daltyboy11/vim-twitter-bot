import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('tweets.db')
    c = conn.cursor()
    c.execute('''
    create table tweets (
        id integer primary key,
        category varchar(255) not null,
        subcategory varchar(255) null,
        tweet varchar(280) not null,
        tweet_date datetime null
    );
    ''')
    conn.commit()
    conn.close()
