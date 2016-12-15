#About#

These scripts are all designed to work by themselves. This is the reason for the duplicate code between them.

##spotify_get.py##

This script takes a list of spotify IDs, and prints info for all the given ids. Or you can give it a single ID as a command line argument.
It was created to ease the use of the 'search'-function in MPC.

The script works for tracks, albums and artists.

###Usage:###
This command would take a list of IDs from the trackids.txt text-file:
```bash
cat trackids.txt | python3 spotify_get.py
```

This command would take the single id given as an argument and print info for that id:
```bash
python3 spotify_get.py spotify:track:4H1Q1P3B7k1p1MK6pkWCH6
```

This command takes all the output from the mpc search-function and pipes it through the script.
Printing info for all the hits in the search:
```bash
mpc search artist 'zeds dead' | python3 spotify_get.py
```

##explore_album.py##

This script takes a spotify album-id, and prints artists and tracks related to the given id.

###Usage:###
This commands takes the single id given as a command-line argument, and prints tracks and artists related to that album-id.
```bash
python3 explore_album.py spotify:album:2LZwWAjsqA2xIldp2c6kRX
```
