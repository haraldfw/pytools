#About#

##coverartgetter##
This script downloads cover art for the track ID of the now playing track of mopidy and replaces the image at path `conky_read_path` with that image.
The script uses spotify's API to download the cover art.

###Configuration variables###

`art_directory`: Path to directory to store image-files.

`track_directory`: Path to directory in which to store symlinks to files in `art_directory`.

`conky_read_path`: Path to image-file that is updated when this script is run. 
If you are using conky to display the art, this is the path that conky should read.

`nowplaying_id_file_path`: Path to where the now playing track id is stored.

###Usage###
This is script is intended to be run about once every second or so, with no arguments.

Simply:
`python /path/to/coverartgetter.py`

In conky:
`${execi 1 python3 ~/conkyscripts/coverartgetter.py}`
