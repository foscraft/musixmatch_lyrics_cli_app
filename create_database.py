import sqlite3
from sqlite3 import Error


def create_database():
    """
    Create a new database and 
    -> Pass a name of choice for your database below and 
    table name of your choice.
    Both will be created on the fly.
    """
    conn = None
    try:
        conn = sqlite3.connect('my_database')
    except Error as e:
        print(e)
    return conn


def create_table(conn):
    '''
    Creating the lyrics table
    '''
    c = conn.cursor()
    c.execute('''
            CREATE TABLE IF NOT EXISTS lyrics_table
            ([lyrics] TEXT)
            ''')                 
    conn.commit()

   
def load_song(conn,song):
    '''
    Loading  the song into the table'''
    c = conn.cursor()
    sql = ''' INSERT INTO lyrics_table VALUES(?) '''
    c.execute(sql, [song])             
    conn.commit()