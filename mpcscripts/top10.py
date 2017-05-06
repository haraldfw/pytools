import subprocess
import sys

artists = sys.argv[1:]
for artist in artists:
    artist = str(artist).rstrip('\n')
    cmd = "mpc -f '%file% splitme%artist%' search artist '{0}' | grep ':track:' | grep 'splitme{0}$' | head -10"
    result = subprocess.getoutput([cmd.format(artist)])
    for line in result.split('\n'):
        subprocess.Popen("mpc add {}".format(line),
                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
