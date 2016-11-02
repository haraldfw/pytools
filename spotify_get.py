# coding: utf-8
import json
import re
import sys
import urllib.request

__author__ = 'Harald Floor Wilhelmsen'


def valid_spotify_id(id):
    pattern = r'^spotify:(track|album|artist):[a-zA-Z0-9]*$'
    return re.match(pattern, id)


def get_input():
    if len(sys.argv) > 1:
        id = str(sys.argv[1]).rstrip('\n')
        if valid_spotify_id(id):
            return [id]
        return None

    lines = sys.stdin
    ids = []
    for line in lines:
        line = str(line).rstrip('\n')
        if valid_spotify_id(line):
            ids.append(line)
    return ids


def trunc_artist_list(artist_list):
    output = []
    for artist in artist_list:
        output.append(artist['name'])
    return ', '.join(output)


def get_track_info(track_id):
    response = urllib.request.urlopen('https://api.spotify.com/v1/tracks/{}'.format(track_id)).read().decode('utf-8')
    response = json.loads(response)
    track_title = response['name']
    artists = trunc_artist_list(response['artists'])
    return ' | '.join([track_title, artists])


def get_album_info(album_id):
    response = urllib.request.urlopen('https://api.spotify.com/v1/albums/{}'.format(album_id)).read().decode('utf-8')
    response = json.loads(response)
    album_name = response['name']
    artists = trunc_artist_list(response['artists'])
    return '; '.join([album_name, artists])


def get_artist_info(artist_id):
    response = urllib.request.urlopen('https://api.spotify.com/v1/artists/{}'.format(artist_id)).read().decode('utf-8')
    response = json.loads(response)
    return response['name']


def get_info(id):
    splits = str(id).split(':')
    type = splits[1]
    id = splits[2]
    if type == 'track':
        return get_track_info(id)

    if type == 'album':
        return get_album_info(id)

    if type == 'artist':
        return get_artist_info(id)

    return ''


def get_spotify_info(ids):
    output = []
    for id in ids:
        id = str(id).rstrip('\n')
        if valid_spotify_id(id):
            output.append(' '.join([id, get_info(id)]))
        else:
            output.append(id)
    if not output:
        return None
    return '\n'.join(output)


def main():
    ids = get_input()
    if ids:
        print(get_spotify_info(ids))


main()
