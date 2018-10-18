import sys
import spotipy
import spotipy.util as util
import csv
from spotipy_helpers import flatten

if __name__ == '__main__':
    if len(sys.argv) > 3:
        username = sys.argv[1]
        client_id = sys.argv[2]
        client_secret = sys.argv[3]
    else:
        print("usage: python playlist_csv.py [username] [client_id] [client_secret]")        
        sys.exit()

token = util.prompt_for_user_token(
    username=username,
    scope='playlist-read-private',
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri='https://example.com/callback/'
)

with open('playlists.csv', 'w', newline='', encoding="utf-8") as csvfile:
    fieldnames = [] #use spotify api to find a list of the fieldnames for playlists    

    if token:
        sp = spotipy.Spotify(auth=token)
        paging = sp.user_playlists(username)
        for playlist_key in flatten(paging['items'][0]):
            fieldnames.append(playlist_key)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for playlist in paging['items']:
            writer.writerow(flatten(playlist))
        print("Finished creating CSV")
    else:
        print("Can't get token for %s" %username)