#About#

##coverartgetter##
This script downloads cover-art for the given track ID. The given track iD has to be from spotify.
The script uses spotify's API to download the cover-art.

Configuration variables:

`art_directory`: Path to directory to store image-files.

`track_directory`: Path to directory in which to store symlinks to files in `art_directory`.

`conky_read_path`: Path to image-file that that is updated when this script is run. If you are using conky to display the art, this is the path that conky should read.

`nowplaying_id_file_path`: Path to where the now playing track id is stored.
