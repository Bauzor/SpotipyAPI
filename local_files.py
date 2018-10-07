"""This script searches for all the songs and artists in a playlist using Spotify Web Api"""

import sys
import spotipy
import spotipy.util as util
import csv

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("  %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name']))
        


def write_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        

if __name__ == '__main__':
    if len(sys.argv) > 3:
        username = sys.argv[1]
        client_id = sys.argv[2]
        client_secret = sys.argv[3]

    else:
        print("Whoops, need your username!")
        print("usage: python local_files.py [username]")
        sys.exit()

token = util.prompt_for_user_token(
    username=username,
    scope='playlist-read-private',
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri='https://example.com/callback/'
)

if token:
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['owner']['id'] == username:
            print(playlist['name'])
            print('%d total tracks' % playlist['tracks']['total'])
            results = sp.user_playlist(username, playlist['id'],
                fields ='tracks,next')
            tracks = results['tracks']
            show_tracks(tracks)
            while tracks['next']:
                tracks = sp.next(tracks)
                show_tracks(tracks)
else:
    print("Can't get token for", username)
