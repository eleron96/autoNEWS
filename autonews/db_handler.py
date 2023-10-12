import sqlite3
import os

DB_NAME = "autonews.db"

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(os.path.join(os.getcwd(), DB_NAME))
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table():
    conn = create_connection()
    try:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS summaries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                author TEXT NOT NULL,
                summary TEXT NOT NULL,
                date TEXT NOT NULL,
                article_title TEXT,
                article_link TEXT
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def insert_summary(author, summary, date, article_title, article_link):
    conn = create_connection()
    try:
        c = conn.cursor()
        c.execute('''
            INSERT INTO summaries (author, summary, date, article_title, article_link)
            VALUES (?, ?, ?, ?, ?)
        ''', (author, summary, date, article_title, article_link))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def get_summaries():
    conn = create_connection()
    summaries = []
    try:
        c = conn.cursor()
        c.execute('SELECT * FROM summaries')
        summaries = c.fetchall()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return summaries
