import subprocess


def get_playlist_files(max_amount=-1, start_index=0):
    playlist = subprocess.getoutput('mpc playlist -f %file%').split('\n')
    playlist_len = len(playlist)
    tracks = []
    index = start_index
    if max_amount < 0:
        max_amount = playlist_len
    while True:
        if index > playlist_len - 1 or len(tracks) >= max_amount:
            break
        file = playlist[index]
        if file.find('spotify:track:') > -1:
            tracks.append(file)
        index += 1
    return tracks
