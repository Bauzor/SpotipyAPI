"""This is a script to search for public information in Spotify"""

import spotipy
import spotipy.oauth2 as oauth2

credentials = oauth2.SpotifyClientCredentials(
    client_id='',
    client_secret='')

token = credentials.get_access_token()
sp = spotipy.Spotify(auth=token)

results = sp.search(q='weezer', limit=20)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])
