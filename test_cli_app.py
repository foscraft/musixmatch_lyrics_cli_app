import os
import sqlite3
import unittest
from unittest.mock import MagicMock, Mock

import pandas as pd
import requests
from dotenv import load_dotenv

from check_database_data import show_lyrics_in_db
from create_database import create_database, create_table, load_song
from lyrics_finder import lyrics_finder

load_dotenv()


class CliAppTests(unittest.TestCase):
    def test_create_db(self) -> None:
        sqlite3.connect = MagicMock(return_value="connection successful")
        dbc = create_database()
        sqlite3.connect.assert_called_with("reuben_database")
        self.assertEqual(dbc, "connection successful")

    def test_create_table(self) -> None:
        # conn = create_database()
        # self.assertTrue(create_table(conn),)
        pass

    def test_load_song(self) -> None:
        pass

    def test_lyrics_finder(self) -> None:
        self.assertIsInstance(lyrics_finder(), dict)

    def test_status(self) -> None:
        call = (
            os.getenv("base_url")
            + os.getenv("lyrics_matcher")
            + os.getenv("format_url")
            + os.getenv("artist_search")
            + "jay z"
            + os.getenv("song_search")
            + "444"
            + os.getenv("api_key")
        )
        resp = requests.get(call)
        self.assertEqual(resp.status_code, 200)

    def test_show_lyrics_in_db(self) -> None:
        # self.assertTrue(show_lyrics_in_db(), type(show_lyrics_in_db())==pd.DataFrame)
        pass


if __name__ == "__main__":
    unittest.main()
