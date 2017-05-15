import sys

import spotipy
from builtins import round
from spotipy.oauth2 import SpotifyClientCredentials


def get_keys():
    home_path = '/home/staff/drift/'
    try:
        with open(home_path + 'spotify.id', 'r') as file:
            client_id = file.readline().rstrip('\n')
        with open(home_path + 'spotify.secret', 'r') as file:
            client_secret = file.readline().rstrip('\n')
    except FileNotFoundError:
        print('Files spotify.id and spotify.secret not found in', home_path, '. Enter keys manually:')
        client_id = input('Client id: ')
        client_secret = input('Client secret: ')
    return client_id, client_secret


def get_spotify(client_id=None, client_secret=None):
    if not client_id or not client_secret:
        client_id, client_secret = get_keys()
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id,
                                                          client_secret=client_secret)
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_seeded_tracks(seed_tracks, limit=20, spotify=None, attrs=True):
    if not spotify:
        spotify = get_spotify()
    tracks = []

    if attrs:
        attributes = get_avg_track_features(seed_tracks, spotify)
        response = spotify.recommendations(
            seed_tracks=seed_tracks,
            limit=limit, country='NO', **attributes)
    else:
        response = spotify.recommendations(seed_tracks=seed_tracks, limit=limit, country='NO')

    for track in response['tracks']:
        tracks.append(track['uri'])
    return tracks


def get_avg_track_features(ids, spot=None):
    if not spot:
        spot = get_spotify()
    average_features = {
        'acousticness': 0,
        'danceability': 0,
        'energy': 0,
        'instrumentalness': 0,
        'liveness': 0,
        'loudness': 0,
        'speechiness': 0,
        'tempo': 0,
        'valence': 0,
        'mode': 0
    }
    response_dicts = spot.audio_features(ids)
    for k, v in average_features.items():
        for track_features in response_dicts:
            average_features[k] += track_features[k]

    for k, v in average_features.items():
        average_features[k] /= len(response_dicts)

    average_features['mode'] = round(average_features['mode'])

    return average_features


if __name__ == '__main__':
    tracks = [
        'spotify:track:04nGzKOAcyzh9DEebAuMV7',
        'spotify:track:2Cpkxl94ijKgxt3Weisfz0',
        'spotify:track:7CotyU8EcChJlqOFnxPPmI'
    ]
    spot = get_spotify(client_id=sys.argv[1], client_secret=sys.argv[2])
    print(*get_seeded_tracks(tracks, spotify=spot))
