import subprocess
import sys

artists = sys.argv[1:]
for artist in artists:
    artist = str(artist).rstrip('\n')
    cmd = "mpc -f '%file% %artist%' search artist '{0}' | grep track | grep '{0}$' | head -10"
    result = subprocess.run([cmd.format(artist)], stdout=subprocess.PIPE)
    for line in result.stdout.decode('utf-8'):
        subprocess.Popen("mpc add {}".format(line),
                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
