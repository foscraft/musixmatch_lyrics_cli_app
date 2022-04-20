import sqlite3
import pandas as pd

conn = sqlite3.connect('musixmatch_database') 
c = conn.cursor()
                   
c.execute('''
          SELECT * FROM lyrics_table
          ''')
df = pd.DataFrame(c.fetchall(), columns=['lyrics'])
print (df)