import sys

from spottylib import get_seeded_tracks
from mpclib import get_playlist_files


def main():
    start_index = 0
    amount = 5
    if len(sys.argv) > 1:
        if str(sys.argv[1]).find('h') > -1:
            print('Gets recommendations from spotify based on tracks from playlist.\n'
                  'Goes trough the playlist and gets <amount> recommended tracks for every chunk of 5 songs after '
                  '<start_index>.\n\n'
                  'usage: python3 radioqloop.py <start_index> <amount>\n\n'
                  'Optional arguments:\n'
                  'start_index: where to start getting seed-tracks from the playlist. Default=0.\n'
                  'amount: how many recommended tracks to get for every five tracks in playlist. CAREFUL WITH THIS. '
                  'Default=5 min=1 max=100')
            return
        start_index = int(sys.argv[1])
    if len(sys.argv) > 2:
        amount = int(sys.argv[2])

    tracks = []
    while True:
        seeds = get_playlist_files(5, start_index)
        if not seeds:
            break
        t = get_seeded_tracks(seeds, amount)
        tracks += t
        start_index += 5

    print('\n'.join(tracks))

if __name__ == '__main__':
    main()
