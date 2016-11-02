##Spotify Get##

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

This command takes all the output from the mpcs search-function and pipes it through the script:
```bash
mpc search artist 'zeds dead' | python3 spotify_get.py
```
