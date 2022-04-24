import requests

from api_key import api_key
import json
from check_database_data import show_lyrics_in_db
from create_database import create_database,create_table, load_song
from api_lyrics import base_url,lyrics_matcher, format_url, artist_search, song_search  
from figlet import figs_cli


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
    print(figs_cli())
    artist_name = input("Whats's the name of the artist? > ")
    song_title = input("What's the name of the song? > ")
    print('-'*50)
    call = base_url + lyrics_matcher + format_url + artist_search + artist_name + song_search + song_title + api_key
    request = requests.get(call)
    data = request.json()
    data = data['message']['body']
    return data['lyrics']['lyrics_body']


def main():
    #reading the lyrics on cli
    song = lyrics_finder()
    print(song)
    saving = input("Do you want to save the lyrics? (y/n): ")
    if saving == "y":

        #create_musixmatch_database 
        conn = create_database()
        #creating lyrics table
        create_table(conn)
        # adding song lyrics to table
        load_song(conn,song)
        print("Song lyrics saved, Bye!")
    else:
        print("Bye!")

    view = input('Would you like to see the lyrics in the database? (y/n)>')
    if view == 'y':
        print('Here are the lyrics in the database:')
        print(show_lyrics_in_db())
    else:
        print('Thank you for using the app')

    

if __name__ == '__main__':
    main()
