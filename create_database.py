import sqlite3
from sqlite3 import Error


def create_database():
    """
    Create a new database and 
    -> Pass a name of your choice for the database below.
    DB Will be created on the fly.
    """
    conn = None
    try:
        conn = sqlite3.connect('new_database')
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    '''
    Creating the lyrics table
    -> Pass a name of your choice for the table.
    Table will be created on the fly.
    '''
    c = conn.cursor()
    c.execute('''
            CREATE TABLE IF NOT EXISTS lyrics_table
            ([artist] TEXT, [title] TEXT, [lyrics] TEXT)
            ''')                 
    conn.commit()

   
def load_song(conn,artist,title,song):
    '''
    Loading  the song into the table'''
    c = conn.cursor()
    sql = ''' INSERT INTO lyrics_table VALUES(?,?,?) '''
    c.execute(sql, [artist,title,song])             
    conn.commit()