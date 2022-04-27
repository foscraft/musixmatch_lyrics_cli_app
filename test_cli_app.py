import pandas as pd
import unittest
import sqlite3
import requests
from unittest.mock import MagicMock, Mock 
from lyrics_finder import  lyrics_finder
from create_database import create_database,create_table, load_song
from api_lyrics import base_url,lyrics_matcher, format_url, artist_search, song_search
from api_key import api_key
from check_database_data import show_lyrics_in_db

class CliAppTests(unittest.TestCase):

    def test_create_db(self):
        sqlite3.connect = MagicMock(return_value='connection successful')
        dbc = create_database()
        sqlite3.connect.assert_called_with('reuben_database')
        self.assertEqual(dbc,'connection successful')

    def test_create_table(self):
        #conn = create_database()
        #self.assertTrue(create_table(conn),)
        pass

    def test_load_song(self):
        pass

    def test_lyrics_finder(self):
        self.assertTrue(lyrics_finder(),type(lyrics_finder())==dict)
        
    def test_status(self):
        call = base_url + lyrics_matcher + format_url + artist_search + 'jay z' + song_search + '444' + api_key
        resp = requests.get(call)
        self.assertEqual(resp.status_code, 200)

    def test_show_lyrics_in_db(self):
        #self.assertTrue(show_lyrics_in_db(), type(show_lyrics_in_db())==pd.DataFrame)
        pass

if __name__ == '__main__':
    unittest.main()