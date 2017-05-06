import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def get_keys():
    home_path = '/home/staff/drift/'
    with open(home_path + 'spotify.id', 'r') as file:
        client_id = file.readline().rstrip('\n')
    with open(home_path + 'spotify.secret', 'r') as file:
        client_secret = file.readline().rstrip('\n')
    return client_id, client_secret


def get_spotify():
    client_id, client_secret = get_keys()
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id,
                                                          client_secret=client_secret)
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_seeded_tracks(seed_tracks, limit=20, spotify=None):
    if not spotify:
        spotify = get_spotify()
    tracks = []
    for hit in spotify.recommendations(seed_tracks=seed_tracks, limit=limit, country='NO')['tracks']:
        tracks.append(hit['uri'])
    return tracks
