from calendar import c
from re import M
import unittest
import sqlite3
import requests
from unittest.mock import MagicMock, Mock 
from lyrics_finder import  lyrics_finder
from create_database import create_database,create_table, load_song
from api_lyrics import base_url,lyrics_matcher, format_url, artist_search, song_search
from api_key import api_key

class CliAppTests(unittest.TestCase):

    def test_create_db(self):
        sqlite3.connect = MagicMock(return_value='connection successful')
        dbc = create_database()
        sqlite3.connect.assert_called_with('my_database')
        self.assertEqual(dbc,'connection successful')

    def test_create_table(self):
        pass

    def test_load_song(self):
        pass

    def test_lyrics_finder(self):
        self.assertTrue(lyrics_finder(),type(lyrics_finder())==dict)

if __name__ == '__main__':
    unittest.main()