import sys

from util import spotify_open_urls_to_file

if __name__ == "__main__":
    print('\n'.join(spotify_open_urls_to_file(sys.stdin)))
