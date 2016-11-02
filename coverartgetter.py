# coding: utf-8
__author__ = 'Harald Floor Wilhelmsen'

import json
import os
import subprocess
import urllib.request

art_directory = "/home/infoskjerm/conkyscripts/art/"
track_directory = "/home/infoskjerm/conkyscripts/tracks/"
art_file_ext = '.png'
conky_read_path = '/tmp/nowplaying.png'
nowplaying_id_file_path = '/tmp/nowplaying.trackid'


def get_track_data(trackid):
    response = urllib.request.urlopen("https://api.spotify.com/v1/tracks/" + trackid).readall().decode('utf-8')
    return json.loads(response)


def trunc_mpd_file(mpdfile):
    return mpdfile[len("spotify:track:"):]


def update_now_playing(trackid):
    art_path = track_directory + trackid
    if not os.path.exists(art_path):
        download_art(trackid)
    with open(nowplaying_id_file_path, 'r') as trackid_file:
        nowplaying = trackid_file.readline().replace('\n', '').strip()
        #print(nowplaying)
    with open(nowplaying_id_file_path, 'w') as trackid_file:
        if not nowplaying or trackid not in nowplaying:
            trackid_file.write(trackid)
            os.unlink(conky_read_path)
            os.symlink(art_path, conky_read_path)
            trackid_file.write(trackid)


def download_art(trackid):
    art_url = get_track_data(trackid)['album']['images'][0]['url']
    art_id = art_url.split('/')[-1]
    art_file = art_directory + art_id + art_file_ext
    if os.path.exists(art_file):
        os.symlink(art_file, track_directory + trackid)
    else:
        urllib.request.urlretrieve(art_url, art_file)
        os.symlink(art_file, track_directory + trackid)


def main():
    open(nowplaying_id_file_path, 'a').close()
    open(conky_read_path, 'a').close()
    spottypw = open('/home/infoskjerm/conkyscripts/spotty-pw').readline().replace('\n', '')
    mpc_return = subprocess.check_output('mpc -f %file% -h ' + spottypw + '@spotty.tihlde.org',
                                         shell=True).decode('utf-8')
    lines = mpc_return.split('\n')
    status = lines[1]
    if status.find('playing') != -1 or status.find('paused') != -1:
        update_now_playing(trunc_mpd_file(lines[0]))


main()
