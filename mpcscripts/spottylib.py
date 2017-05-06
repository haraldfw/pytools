import subprocess

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


def get_seeds_from_playlist(start_index=0, amount=5):
    if amount > 5:  # 5 is hard limit for track-seeds
        amount = 5
    playlist = subprocess.getoutput('mpc playlist -f %file%').split('\n')
    tracks = []
    index = start_index
    while True:
        if index > len(playlist) - 1 or index > start_index + amount:
            break
        file = playlist[index]
        if file.find('spotify:track:') > -1:
            tracks.append(file)
    return tracks


def get_seeded_tracks(seed_tracks, amount=20, spotify=None):
    if not spotify:
        spotify = get_spotify()
    tracks = []
    for hit in spotify.recommendations(seed_tracks=seed_tracks, limit=amount, country='NO')['tracks']:
        tracks.append(hit['uri'])
    return tracks
