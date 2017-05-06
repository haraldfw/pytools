import sys

from spottylib import get_seeds_from_playlist, get_seeded_tracks

if __name__ == '__main__':
    start_index = 0
    amount = 5
    if len(sys.argv) > 1:
        start_index = int(sys.argv[1])
    if len(sys.argv) > 2:
        amount = int(sys.argv[2])

    seeds = get_seeds_from_playlist(start_index, amount)
    print(get_seeded_tracks(seeds))
