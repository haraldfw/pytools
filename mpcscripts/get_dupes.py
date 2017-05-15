import mpclib


def parse_queue(queue):
    tracks = []
    dupes = []
    i = 1
    for track in queue:
        if track not in tracks:
            tracks.append(track)
        else:
            dupes.append(i)
        i += 1
    dupes.sort(reverse=True)
    return dupes



if __name__ == '__main__':
    print(*parse_queue(mpclib.get_playlist_files()), sep='\n')