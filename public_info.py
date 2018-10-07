"""This is a script to search for public information in Spotify"""

import spotipy
import spotipy.oauth2 as oauth2

credentials = oauth2.SpotifyClientCredentials(
    client_id='3801b7a3963441268f44c75aa830c9e2',
    client_secret='db16260604104561b23fd2cd98ca54ce')

token = credentials.get_access_token()
sp = spotipy.Spotify(auth=token)

results = sp.search(q='weezer', limit=20)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])
