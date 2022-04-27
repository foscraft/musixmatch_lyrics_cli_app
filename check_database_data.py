import sqlite3
import pandas as pd

def show_lyrics_in_db():
    conn = sqlite3.connect('new_database')
    c = conn.cursor()
    c.execute('''
            SELECT * FROM lyrics_table
            ''')
    return pd.DataFrame(c.fetchall(), columns=['artist','title','lyrics'])