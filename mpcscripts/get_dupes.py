import mpclib


def get_dupes(queue):
    tracks = []
    dupes = []
    i = 1
    for track in queue:
        if track not in tracks:
            tracks.append(track)
        else:
            dupes.append(i)
        i += 1
    return dupes


if __name__ == '__main__':
    dupes = get_dupes(mpclib.get_playlist_files())
    dupes.sort(reverse=True)
    print(*dupes, sep='\n')
