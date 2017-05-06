import subprocess

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def get_keys():
    home_path = '/home/staff/drift/'
    with open(home_path + 'spotify.id', 'r') as file:
        client_id = file.read()
    with open(home_path + 'spotify.secret', 'r') as file:
        client_secret = file.read()
    return client_id, client_secret


def get_spotify():
    client_id, client_secret = get_keys()
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id,
                                                          client_secret=client_secret)
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_spotify_test():
    client_credentials_manager = SpotifyClientCredentials(client_id='1cca5549d1b84fc2aca1a6c3650e7d07',
                                                          client_secret='814c42749096465d9245e15bdcbea20f')
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_seeds_from_playlist(start_index=0, amount=5):
    if amount > 5:  # 5 is hard limit for track-seeds
        amount = 5
    playlist = subprocess.getoutput('mpc playlist -f %file%').split('\n')
    tracks = []
    for index in range(start_index, start_index + amount):
        if index > len(playlist):
            break
        tracks.append(playlist[index])


def get_seeded_tracks(seed_tracks, amount=20, spotify=None):
    if not spotify:
        spotify = get_spotify()
    tracks = []
    for hit in spotify.recommendations(seed_tracks=seed_tracks, limit=amount)['tracks']:
        tracks.append(hit['uri'])
    return tracks
