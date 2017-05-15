import sys

from spottylib import get_spotify, get_top_tracks

artists = sys.argv[1:]
spotify = get_spotify()
for spotify_id in artists:
    print(*get_top_tracks(spotify_id, spotify), sep='\n')
