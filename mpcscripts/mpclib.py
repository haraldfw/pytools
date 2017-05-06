import subprocess


def get_playlist_files(max_amount, start_index=0):
    playlist = subprocess.getoutput('mpc playlist -f %file%').split('\n')
    tracks = []
    index = start_index
    while True:
        if index > len(playlist) - 1 or len(tracks) >= max_amount:
            break
        file = playlist[index]
        if file.find('spotify:track:') > -1:
            tracks.append(file)
        index += 1
    return tracks