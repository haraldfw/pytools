import sys

import requests

from spottylib import get_seeded_tracks
from mpclib import get_playlist_files


def radioq(start_index, amount):
    seeds = get_playlist_files(5, start_index)
    return get_seeded_tracks(seeds, amount)


def radioq_loop(start_index, amount):
    tracks = []
    while True:
        seeds = get_playlist_files(5, start_index)
        if not seeds:
            break
        t = get_seeded_tracks(seeds, amount)
        tracks += t
        start_index += 5
    return tracks


def contains_either(val, searches):
    contains = False
    val = str(val)
    for search in searches:
        if val.find(search) > -1:
            contains = True
    return contains


def parse_args():
    args = {}
    sys.argv.pop(0)
    for i in range(len(sys.argv)):
        val = sys.argv[i]
        if contains_either(val, ['-l', '--loop']):
            args['loop'] = True
        elif contains_either(val, ['-s', '--start-index']):
            args['start_index'] = int(sys.argv[i + 1])
            i += 1
        elif contains_either(val, ['-a', '--amount']):
            args['amount'] = int(sys.argv[i + 1])
            i += 1
        elif contains_either(val, ['-h', '--help']):
            args['help'] = True
    return args


def help():
    print('Gets recommendations from spotify based on tracks from playlist.\n\n'
          'usage: python3 radioq.py <start_index> <amount>\n\n'
          'Flags:\n'
          '\t-l, --loop\n\t\tEnable looping. Enabling this will make the script go through the playlist and get '
          '<amount> recommended tracks for every chunk of 5 tracks. This is time-consuming, and might spam '
          'your queue.\n'
          '\t-s, --start-index\n\t\tSpecify where to start getting seed-tracks from the playlist. Default=0.\n'
          '\t-amount, --amount\n\t\tSpecify amount of recommended tracks to get. Default=20 min=1 max=100.\n'
          '\t-h, --help\n\t\tOutputs this information.\n')


def main():
    try:
        args = parse_args()
    except ValueError:
        print('Something went wrong when parsing your args.\nFor help: python3')
        help()
        return

    if 'help' in args:
        help()
        return

    start_index = 0
    amount = 20
    if 'start-index' in args:
        start_index = args['start-index']

    if 'amount' in args:
        amount = args['amount']

    try:
        if 'loop' in args:
            tracks = radioq_loop(start_index, amount)
        else:
            tracks = radioq(start_index, amount)
    except requests.exceptions.HTTPError:
        print('Something went wrong when getting seeds. Check your command and try again. ')
        return

    print('\n'.join(tracks))

if __name__ == '__main__':
    main()
