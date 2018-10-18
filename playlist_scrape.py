import sys
import spotipy
import spotipy.util as util
import csv


if __name__ == "__main__":
    if (len(sys.argv) > 3):
        username = sys.argv[1]
        client_id = sys.argv[2]
        client_secret = sys.argv[3]
    else:
        print("usage: playlist_scrape.py [username] [client_id] [client_secret]")
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
    paging = sp.user_playlists(username)
    
    print("\n")
    for playlist in paging['items']:
        print(playlist['name'],"\n")
    selected_PL = input("Please choose a playlist you would like to create a dataset with:\n")
    
    for playlist in paging['items']:
        if selected_PL == playlist['name']:
            chosenPL = sp.user_playlist(playlist['owner']['id'], playlist_id=playlist['id'])

    with open('%s' % selected_PL, 'w', newline='', encoding='utf-8'):
        fieldnames=[]

        print(chosenPL['tracks']['items'][0])
else:
    print("token not authorized")