# coding: utf-8
import sys

import re

__author__ = 'Harald Floor Wilhelmsen'

def valid_spotify_id(id):
    pattern = '^spotify:(track|album|artist):[a-zA-Z0-9]*$'
    return re.match(pattern, id)


def get_input():
    """
    Returns the input from the user. Will be of the format of a spotify id-string.
    :return: The spotify id-string. None if stdin or argv is empty or of wrong format.
    """
    if len(sys.argv) > 1:
        id = str(sys.argv[1]).rstrip('\n')
        if valid_spotify_id(id):
            return [id]
        return None

    lines = sys.stdin
    ids = []
    for line in lines:
        line = str(line)
        line = line.rstrip('\n')
        if valid_spotify_id(line):
            ids.append(line)

    return None


def call_spotify(ids):
    for id in ids:
        splits = str(id).split(':')



def main():
    id_ar = get_input()
    if id_ar:
        print('spotify id: ' + id_ar[0])
        print('match: {}'.format(valid_spotify_id(id_ar[0])))


main()
