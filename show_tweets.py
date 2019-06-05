import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('tweets.db')
    c = conn.cursor()
    c.execute('select * from tweets;')
    conn.commit()
    print(c.fetchall())
