import sys

from spottylib import get_seeded_tracks
from mpclib import get_playlist_files


def main():
    start_index = 0
    amount = 20
    if len(sys.argv) > 1:
        if str(sys.argv[1]).find('h') > -1:
            print('Gets recommendations from spotify based on tracks from playlist.\n\n'
                  'usage: python3 radioq.py <start_index> <amount>\n\n'
                  'Optional arguments:\n'
                  'start_index: where to start getting seed-tracks from the playlist. Default=0.\n'
                  'amount: how many recommended tracks to get. Default=20 min=1 max=100')
            return
        start_index = int(sys.argv[1])
    if len(sys.argv) > 2:
        amount = int(sys.argv[2])

    seeds = get_playlist_files(5, start_index)
    if not seeds:
        print('Something went wrong when getting seeds. Check your command and try again.')
        return
    print('\n'.join(get_seeded_tracks(seeds, amount)))

if __name__ == '__main__':
    main()
