import sys
import spotipy
import spotipy.util as util
import csv
from spotipy_helpers import flatten


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

    with open('%s.csv' % selected_PL, 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames=[]
        non_local = 0
        while(chosenPL['tracks']['items'][non_local]['is_local']):
            non_local += 1
        for key in flatten(chosenPL['tracks']['items'][non_local]):
            fieldnames.append(key)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for track in chosenPL['tracks']['items']:
            writer.writerow(flatten(track))
        next_page = sp.next(chosenPL['tracks'])
        while(next_page):
            for track in next_page['items']:
                writer.writerow(flatten(track))
            next_page = sp.next(next_page)
else:
    print("token not authorized")