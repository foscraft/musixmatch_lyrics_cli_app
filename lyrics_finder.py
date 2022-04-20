import requests
from api_lyrics import *
import json
import sqlite3
from sqlite3 import Error

def lyrics_finder():

    '''
    TODO:
    Leverage Musixmatch API to create an interactive CLI app that allows the user to key in
    a search query of a song. If the song is found on Musixmatch database, please display
    the lyrics to the user.
    Give the user a menu where they can choose to search or view saved song lyrics.
    You can ask a user whether they want to save their search results. If so, store the lyrics
    in a local SQLite database.
    '''
    artist_name = input("Whats's the name of the artist? > ")
    track_name = input("What's the name of the track? > ")
    print('-----------------------------------------')
    api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
    request = requests.get(api_call)
    data = request.json()
    data = data['message']['body']
    print(f"API Call: {api_call}")
    print()
    return data['lyrics']['lyrics_body']


def create_connection(song_db_file):
    """ create a database connection to the SQLite database
        specified by song_db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(song_db_file)
    except Error as e:
        print(e)

    return conn


def create_lyric_project(conn, lyric_project):
    """
    Create a new project into the projects table
    :param conn:
    :param lyric_project:
    :return: lyric_project id
    """
    sql = ''' INSERT INTO lyric_project(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, lyric_project)
    conn.commit()
    return cur.lastrowid


def load_song(conn, songs):
    """
    load a new song into the songs table
    :param conn:
    :param songs:
    :return:
    """

    '''
    Pass  the returned lyrics
    '''
    
    sql = ''' INSERT INTO songs(lyrics,name)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, songs)
    conn.commit()
    return cur.lastrowid


def main():
    #reading the lyrics on cli
    print(lyrics_finder())
    saving = input("Do you want to save the lyrics? (y/n): ")
    if saving == "y":

        database = r"/home/foscraft/miniconda3/bin/sqlite3.db"

        # creating a database connection
        conn = create_connection(database)
        with conn:
            # creating a new lyric_project
            lyric_project = ('Song lyrics finder with python sqlite3', '2022-04-14', '2022-04-22');
            project_id = create_lyric_project(conn, lyric_project)

            # songs
            lyrics = lyrics_finder()
            song = (lyrics)       

            # load songs
            load_song(conn, song)
            print("Song lyrics saved, Bye!")
    else:
        print("Thank you for using the app")


if __name__ == '__main__':
    main()




    # # check if the user wants to go again
    # print()
    # print("Again? (y/n)")
    # again = input("> ")
    # if again == "n":
    #     break
