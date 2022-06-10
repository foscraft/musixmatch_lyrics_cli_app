import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

from check_database_data import show_lyrics_in_db
from create_database import create_database, create_table, load_song
from figlet import figs_cli

load_dotenv()

api_key = os.getenv("api_key")


def lyrics_finder() -> Any:

    """
    TODO:
    Leverage Musixmatch API to create an interactive CLI app that allows the user to key in
    a search query of a song. If the song is found on Musixmatch database, please display
    the lyrics to the user.
    Give the user a menu where they can choose to search or view saved song lyrics.
    You can ask a user whether they want to save their search results. If so, store the lyrics
    in a local SQLite database.
    """
    print(figs_cli())
    artist = input("Whats's the name of the artist? > ")
    title = input("What's the name of the song? > ")
    print("-" * 50)
    call = (
        os.getenv("base_url")
        + os.getenv("lyrics_matcher")
        + os.getenv("format_url")
        + os.getenv("artist_search")
        + artist
        + os.getenv("song_search")
        + title
        + os.getenv("api_key")
    )
    request = requests.get(call)
    data = request.json()
    data = data["message"].get("body")
    if not data:
        print("song not found")
    else:
        return [artist, title, data["lyrics"]["lyrics_body"]]


def main() -> None:
    # reading the lyrics on cli
    song = lyrics_finder()
    if song is not None:
        try:
            print(song[2])
        except TypeError:
            print("song not found")
    saving = input("Do you want to save the lyrics? (y/n): ")
    if saving in ["y", "Y", "yes", "Yes", "YES"]:
        # create_musixmatch_database
        conn = create_database()
        # creating lyrics table
        create_table(conn)
        # adding song lyrics to table
        if song is not None:
            try:
                load_song(conn, song[0], song[1], song[2])
            except TypeError:
                print("no song to be save")
        print("Song lyrics saved, Bye!")
    else:
        print("Bye!")

    view = input("Would you like to see the lyrics in the database? (y/n)>")
    if view in ["y", "Y", "yes", "Yes", "YES"]:
        print("Here are the lyrics in the database:")
        print(show_lyrics_in_db())
    else:
        print("Thank you for using the app")


if __name__ == "__main__":
    main()
