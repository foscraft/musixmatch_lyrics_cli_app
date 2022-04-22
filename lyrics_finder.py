import requests
from api_lyrics import base_url,lyrics_matcher, format_url, artist_search_parameter, track_search_parameter
from api_key import api_key
import json
from create_database import create_musixmatch_database, load_song

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
    track_name = input("What's the name of the song? > ")
    print('-----------------------------------------')
    api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
    request = requests.get(api_call)
    data = request.json()
    data = data['message']['body']
    return data['lyrics']['lyrics_body']


def main():
    #reading the lyrics on cli
    song = lyrics_finder()
    print(song)
    saving = input("Do you want to save the lyrics? (y/n): ")
    if saving == "y":

        #create_musixmatch_database and lyrics table
        create_musixmatch_database()
        # adding song lyrics to table
        load_song(song)
        print("Song lyrics saved, Bye!")
    else:
        print("Thank you for using the app")

if __name__ == '__main__':
    main()
