import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_songs(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, n_songs, scope="user-library-read"):
    if n_songs > 50:
        raise ValueError("Number of songs cannot exceed 50 in the request")
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                             client_secret=SPOTIPY_CLIENT_SECRET, scope=scope, redirect_uri='http://localhost/'))

        results = sp.current_user_saved_tracks(limit=n_songs)
        liked = []
        while results:
            for idx, item in enumerate(results['items']):
                track = item['track']
                liked.append([track['external_urls']['spotify'],
                            track['name'], track['artists'][0]['name']])
            if results['next']:
                results = sp.next(results)
            else:
                results = None

        return liked
    except Exception as e:
        return print(e)