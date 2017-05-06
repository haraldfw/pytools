import sys

from spottylib import get_seeds_from_playlist, get_seeded_tracks

if __name__ == '__main__':
    start_index = 0
    amount = 5
    if len(sys.argv) > 1:
        if str(sys.argv[1]).find('h') > -1:
            print('Gets recommendations from spotify based on tracks from playlist.\n\n'
                  'usage: python3 radioq.py <start_index> <amount>\n\n'
                  'start_index: where to start getting seed-tracks from the playlist.\n'
                  'amount: how many tracks from the playlist (starting at start_index) to use as seeds.')
            sys.exit()
        start_index = int(sys.argv[1])
    if len(sys.argv) > 2:
        amount = int(sys.argv[2])

    seeds = get_seeds_from_playlist(start_index, amount)
    print('\n'.join(get_seeded_tracks(seeds)))
