import signal
import sys

import requests

from mpclib import get_playlist_files
from spottylib import get_seeded_tracks


def radioq(start_index, amount, attrs):
    seeds = get_playlist_files(5, start_index)
    if not seeds:
        print('No seeds found in mpc playlist. Exiting...')
        sys.exit(signal.SIGINT)
    return get_seeded_tracks(seeds, amount, attrs=attrs)


def radioq_loop(start_index, amount, attrs):
    tracks = []
    while True:
        seeds = get_playlist_files(5, start_index)
        if not seeds:
            break
        t = get_seeded_tracks(seeds, amount, attrs=attrs)
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
        elif contains_either(val, ['-n', '--no-attributes']):
            args['no-attributes'] = True
    return args


def print_help():
    print('Gets recommendations from spotify based on tracks from playlist.\n\n'
          'usage: python3 radioq.py [OPTION]...\n\n'
          'Options:\n'
          '\t-l, --loop\n\t\tEnable looping. Enabling this will make the script go through the playlist and get '
          '<amount> recommended tracks for every chunk of 5 tracks. This is time-consuming, and might spam '
          'your queue.\n'
          '\t-s, --start-index\n\t\tSpecify where to start getting seed-tracks from the playlist. Default=0.\n'
          '\t-a, --amount\n\t\tSpecify amount of recommended tracks to get. Default=20 min=1 max=100.\n'
          '\t-h, --help\n\t\tOutputs this information.\n',
          '\t-n, --no-attributes\n\t\tDisable getting audio features. This makes the script faster, but '
          'the results will be worse.\n')


def main():
    try:
        args = parse_args()
    except ValueError:
        print('Something went wrong when parsing your args.\nFor help: python3')
        print_help()
        return

    if 'help' in args:
        print_help()
        return

    start_index = 0
    amount = 20
    if 'start-index' in args:
        start_index = args['start-index']

    if 'amount' in args:
        amount = args['amount']

    attrs = 'no-attributes' not in args

    try:
        if 'loop' in args:
            tracks = radioq_loop(start_index, amount, attrs)
        else:
            tracks = radioq(start_index, amount, attrs)
    except requests.exceptions.HTTPError:
        print('Something went wrong when getting seeds. Check your command and try again. ')
        return

    print('\n'.join(tracks))


if __name__ == '__main__':
    main()
