# coding: utf-8
import json
import re
import sys
import urllib.request

__author__ = 'Harald Floor Wilhelmsen'


def join_artist_list(artist_list):
    output = []
    for artist in artist_list:
        output.append(artist['name'])
    return ', '.join(output)


def valid_spotify_id(id):
    pattern = r'^spotify:(track|album|artist):[a-zA-Z0-9]*$'
    return re.match(pattern, id)


def join_track_list(track_list):
    tracks = []
    for track in track_list:
        tracks.append(track['name'])
    return '\n'.join(tracks)


def get_album_info(album_id):
    response = urllib.request.urlopen('https://api.spotify.com/v1/albums/{}'.format(album_id)).read().decode('utf-8')
    response = json.loads(response)
    album_name = response['name']
    artists = join_artist_list(response['artists'])
    tracks = join_track_list(response['tracks']['items'])
    info = ' | '.join([album_name, artists])
    return '\n'.join([info, tracks])


def get_input():
    if len(sys.argv) > 1:
        id = str(sys.argv[1]).rstrip('\n')
        if valid_spotify_id(id):
            return id
        print('Argument given in command-line was not a valid spotify id.')


def main():
    id = str(get_input())
    if id and valid_spotify_id(id):
        splits = str(id).split(':')
        print(' '.join([id, get_album_info(splits[2])]))


main()
