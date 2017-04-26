import subprocess
import sys

artists = sys.argv[1:]
for artist in artists:
    artist = str(artist).rstrip('\n')
    subprocess.Popen("mpc search artist '{}' | grep track | head -10 | mpc add".format(artist),
                     shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
