#base url
base_url = "https://api.musixmatch.com/ws/1.1/"

# api method for getting lyrics
lyrics_matcher = "matcher.lyrics.get"

# format url
format_url = "?format=json&callback=callback"

# parameters
artist_search = "&q_artist="
song_search = "&q_track="


# full_path = f'https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?format=json&callback=callback&q_artist={artist_name}&q_track={song_title}{api_key}'
#from api_lyrics import base_url,lyrics_matcher, format_url, artist_search, song_search
#call = base_url + lyrics_matcher + format_url + artist_search + artist_name + song_search + track_name + api_key
