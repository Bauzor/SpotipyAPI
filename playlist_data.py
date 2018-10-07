import sys
import spotipy
import spotipy.util as util
import csv

with open('playlists.csv', 'w', newline='') as csvfile:
    fieldnames = [] #use spotify api to find a list of the fieldnames for playlists

if __name__ == '__main__':
    if len(sys.argv) > 3:
        username = sys.argv[1]
        client_id = sys.argv[2]
        client_secret = sys.argv[3]
    else:
        print("usage: python local_files.py [username] [client_id] [client_secret]")        
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
    for key in playlists:
        if key == 'items':
            print(key)
        else:
            print('not items')

else:
    print("Can't get token for %s" %username)