import sys
from spottylib import spotify_open_urls_to_file

if __name__ == "__main__":
    for line in spotify_open_urls_to_file(sys.stdin):
        print(line)
